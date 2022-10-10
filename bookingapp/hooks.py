# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "bookingapp"
app_title = "Booking Service App"
app_publisher = "Jigar Tarpara"
app_description = "Booking Any type of Service"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "jigartarpara68@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/bookingapp/css/bookingapp.css"
# app_include_js = "/assets/bookingapp/js/bookingapp.js"

# include js, css files in header of web template
# web_include_css = "/assets/bookingapp/css/bookingapp.css"
# web_include_js = "/assets/bookingapp/js/bookingapp.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}
doctype_js = {"Item" : "public/js/bookingapp_item.js"}
# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "bookingapp.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "bookingapp.install.before_install"
# after_install = "bookingapp.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "bookingapp.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
    "Item": {
        "validate": "bookingapp.utils.make_booking_service_item"
    }
}
after_migrate = "bookingapp.booking_service_app.doctype.khatavahi_book_service_setting.khatavahi_book_service_setting.setup_custom_fields"
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"bookingapp.tasks.all"
# 	],
# 	"daily": [
# 		"bookingapp.tasks.daily"
# 	],
# 	"hourly": [
# 		"bookingapp.tasks.hourly"
# 	],
# 	"weekly": [
# 		"bookingapp.tasks.weekly"
# 	]
# 	"monthly": [
# 		"bookingapp.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "bookingapp.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "bookingapp.event.get_events"
# }
