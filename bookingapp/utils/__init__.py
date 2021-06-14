from __future__ import with_statement

import datetime
import inspect
import json
import traceback
from io import SEEK_END, SEEK_SET
from typing import Dict

import frappe
from werkzeug.exceptions import BadRequest, NotFound


def api_version(version):
    """API version decorator. Used to indicate a given ApiEndpoint method is a specific API
    version."""

    def inner_version(fn):
        fn.__api_version = version
        return fn

    return inner_version


class ApiEndpoint(object):
    """Base class for all API endpoints."""

    def __init__(self, name, sensitive_keys=None, impersonate_user=False):
        """Initializes the API endpoint with the given name. The name will be used for analytics."""
        self.name = name
        self.sensitive_keys = sensitive_keys if sensitive_keys else []
        self.impersonate_user = impersonate_user
        self.logger = frappe.logger(
            "jahez_api", allow_site=True, file_count=50)
        self.logged_parameter_sources = {}

    def run(self, *args, **kwargs):
        """Entry-point for this endpoint. Parses API version from query string or body and calls
        the appropriate implementation, or the default implementation."""
        self.logger.info('START {}'.format(self.name))

        requested_api_version = None

        if 'api_version' in kwargs:
            requested_api_version = kwargs['api_version']
            self.logger.info(
                'API version ''{}'' from query string'.format(requested_api_version))

        if requested_api_version is None:
            requested_api_version = self.try_get_api_version_from_query_and_body()
            if requested_api_version:
                self.logger.info(
                    'API version ''{}'' from body'.format(requested_api_version))

        self.api_version = requested_api_version
        if requested_api_version is not None:
            method = self.get_method_by_api_version(requested_api_version)
            if not method:
                self.logger.info('Could not find implementation for version ''{}'''.format(
                    requested_api_version))
                return self.respond_with_code(
                    code=400, error_code='InvalidVersion',
                    message="Invalid API Version '{}'".format(
                        requested_api_version)
                )

            result = self.execute(lambda: method(*args, **kwargs))

        else:
            self.logger.info(
                'No API version requested. Executing default version.')
            result = self.execute(lambda: self.default(*args, **kwargs))

        self.logger.info('END {}'.format(self.name))
        return result

    def log_parameters(self, source: str, params: dict):
        # Avoid logging the same source multiple times until we refactor parameter logging
        # TODO: Fix parameter logging to avoid calling it multiple times
        if source in self.logged_parameter_sources:
            return
        self.logged_parameter_sources[source] = True

        logged_params = {}
        if self.sensitive_keys:
            for k, v in params.items():
                if k not in self.sensitive_keys:
                    logged_params.update({k: v})
        else:
            logged_params = params
        self.logger.info(f"parameters ({source}): {logged_params}")

    def default(self):
        """Default endpoint implementation if no API version is specified. Override this in derived
        classes."""
        return self.respond_with_code(code=200, data={})

    def query_string(self):
        """Return a dictionary from the Query string."""
        return frappe.request.args

    def json_body(self):
        """Returns a dictionary parsed from the body as JSON. If the body is not json, returns an
        empty dictionary."""
        body = frappe.request.data or '{}'
        try:
            result = json.loads(body)
        except ValueError:
            result = dict()

        return result

    def form_body(self):
        """Returns a dictionary representing the form body parameters including files."""
        body = frappe.request.form.copy()

        # Add files directly as well. Iterating yields the file parameter names. Indexing with the
        # name yields a werkzeug.datastructures.FileStorage which we use as the value
        for f in frappe.request.files:
            body[f] = frappe.request.files[f]

        return body

    def file_size_in_bytes(self, f):
        f.seek(0, SEEK_END)
        size = f.tell()
        f.seek(0, SEEK_SET)
        return size

    def try_get_api_version_from_query_and_body(self):
        """Attempts to retrieve the API version from the query string, then request body if any. Treats the body as
        JSON first, then form-data if JSON is empty."""
        params = self.query_string()
        if 'api_version' in params:
            return params['api_version']

        params = self.json_body()
        if not params:
            params = self.form_body()

        if 'api_version' in params:
            return params['api_version']

        return None

    def get_method_by_api_version(self, version):
        """Inspects the current object for methods decorated with @api_version and whose declared
        version matches the requested version."""
        methods = [f[1] for f in inspect.getmembers(self, inspect.ismethod) if
                   hasattr(f[1], '__api_version') and str(
                       getattr(f[1], '__api_version')) == str(version)]
        if not methods:
            return None

        return methods[0]

    def validate_date_format(self, dates, date_format="%Y-%m-%d"):
        try:
            for date in dates:
                datetime.datetime.strptime(date, date_format)
            return True
        except ValueError:
            return False

    def validate_required_parameters(self, params, required_parameter_names, alternative_parameters=None):
        """Checks that all keys defined in 'required_parameter_names' exist in 'params', and that
        one of the parameter names in each tuple in 'alternative_parameters' exists in 'params'.
        * params: The incoming parameters from body or query string as a dictionary
        * required_parameter_names: A list of required parameter names
        * alternative_parameters: A list of tuples, each defining the names of alternative parameter
        names (that is, if one of the names in the tuple is defined, the requirement is met)"""
        def check_tuple_parameters(param_tuple):
            for p in param_tuple:
                if p in params and params[p] is not None:
                    return True
            return False

        alternative_parameters = alternative_parameters if alternative_parameters else []

        missing_parameters = [p for p in required_parameter_names if
                              p not in params or params[p] is None]

        missing_alt_parameters = [p for p in alternative_parameters if
                                  not check_tuple_parameters(p)]

        if missing_alt_parameters or missing_parameters:
            message = ''
            if missing_parameters:
                message += 'Required parameters are missing: {}. '.format(
                    ', '.join(missing_parameters))

            if missing_alt_parameters:
                tuples = [' | '.join(x)
                          for x in [p for p in missing_alt_parameters]]
                message += 'Specify at least one of the following: {}'.format(
                    ', '.join(tuples))

            return False, self.respond_with_code(code=400, error_code='ArgumentNotFound',
                                                 message=message)

        return True, None

    def validate_required_parameters_has_vales(self, params, required_parameters):
        missing_values = []
        for p in required_parameters:
            v = params.get(p)
            if v in ['0', '0.0', 0, 0.0]:
                return True, None

            if not v:
                missing_values.append(p)
        if missing_values:
            return False, self.respond_with_code(code=400, error_code='ValuesNotFound',
                                                 message=f"These arguments {missing_values} values can't be empty")
        return True, None

    def validate_input_type(self, input_params: dict, input_type: tuple, check_digit=False):
        wrong_type_values = []
        for k, v in input_params.items():
            if v:
                if not isinstance(v, input_type):
                    wrong_type_values.append(k)
                if str in input_type and check_digit and isinstance(v, str):
                    try:
                        float(v)
                    except ValueError:
                        wrong_type_values.append(k)
        if wrong_type_values:
            return False, self.respond_with_code(error_code="BadRequest",
                                                 developer_message=f"{wrong_type_values} have wrong input type",
                                                 code=400)
        return True, None

    def validate_positive_value(self, input_params: dict):
        negative_value = []
        for k, v in input_params.items():
            if v:
                if float(v) < 0:
                    negative_value.append(k)
        if negative_value:
            return False, self.respond_with_code(error_code="BadRequest",
                                                 developer_message=f"{negative_value} value shouldn't be negative",
                                                 code=400)
        return True, None

    def respond_with_code(
            self,
            message='',
            data=None,
            code=200,
            error_code='',
            exception=None,
            related_doctypes=None,
            developer_message='', sub_dict=None
    ) -> Dict[str, any]:
        """Responds with the standard envelope and the given status code, data, error code,
        and message.
       """
        if sub_dict is None:
            sub_dict = {}
        has_request = frappe.request
        if has_request:
            frappe.local.response.http_status_code = code
        developer_message = developer_message or message

        if exception and not error_code:
            error_code = exception.__class__.__name__

        if error_code and not message:
            error = frappe.get_value("Error Code", {'name': error_code}, ['message', 'http_code'],
                                     as_dict=True)

            if not error:
                message = f"Server Error ({error_code})"
            else:
                message = error.message

                if not code:
                    code = error.http_code

        if error_code:
            org_message = message
            message = frappe._(error_code)
            if message == error_code:
                message = org_message
        else:
            message = frappe._(message)

        self.logger.info(
            f"Respond with: Code = {code}, ErrorCode = {error_code}, Message = {message}, Developer Message = {developer_message}")
        return {
            "message": message,
            "data": data,
            "errorCode": error_code,
            "code": code,
            "developer_message": developer_message
        }

    def execute(self, action):
        """Executes an action and serializes frappe/web exceptions using the standard envelope."""
        try:
            return action()
        except frappe.ValidationError as e:
            traceback.print_exc()
            self.logger.exception('Validation error exception')
            frappe.db.rollback()
            return self.respond_with_code(exception=e, code=417)
        except NotFound as e:
            traceback.print_exc()
            self.logger.exception('Not found exception')
            frappe.db.rollback()
            return self.respond_with_code(exception=e, code=404)
        except BadRequest as e:
            traceback.print_exc()
            self.logger.exception('Bad request exception')
            frappe.db.rollback()
            return self.respond_with_code(exception=e, code=400)
        except (frappe.PermissionError, PermissionError) as e:
            traceback.print_exc()
            self.logger.exception('Permission exception')
            frappe.db.rollback()
            return self.respond_with_code(exception=e, code=403, error_code="Forbidden")
        except frappe.AuthenticationError as e:
            traceback.print_exc()
            self.logger.exception('Authentication exception')
            frappe.db.rollback()
            return self.respond_with_code(exception=e, code=401, error_code="AuthenticationError")
        except Exception as e:
            traceback.print_exc()
            self.logger.exception('Generic exception')
            frappe.db.rollback()
            return self.respond_with_code(exception=e, code=500)
