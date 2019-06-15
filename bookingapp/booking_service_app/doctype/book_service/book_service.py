# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.mapper import get_mapped_doc
from frappe.utils import flt, nowdate, getdate
from frappe.model.document import Document

class BookService(Document):
	def validate(self):
		self.validate_booking_date()

	def validate_booking_date(self):
		for row in self.book_item:
			is_booked = self.check_item_is_booked(row.delivery_date, row.return_date, row.item)
			if is_booked:
				return is_booked
		return ""
	
	def check_item_is_booked(self, delivery_date, return_date, item):
		
		if delivery_date:
			filters = {}
			filters = {'item': item, 'docstatus': 1 }

			filters.update({'delivery_date': ['<=',delivery_date]})
			filters.update({'return_date': ['>=',delivery_date]})
			
			bookings = frappe.get_all('Book Service Item', filters=filters, fields=['name', 'delivery_date', 'return_date', 'parent'])
			
			for booking in bookings:
				return "Already Booked: ID "+ booking.parent

		if return_date:
			filters = {}
			filters = {'item': item, 'docstatus': 1 }
			filters.update({'delivery_date': ['<=',return_date]})
			filters.update({'return_date': ['>=',return_date]})
		
			bookings = frappe.get_all('Book Service Item', filters=filters, fields=['name', 'delivery_date', 'return_date', 'parent'])
			
			for booking in bookings:
				return "Already Booked: ID "+ booking.parent

		if delivery_date and return_date:
			
			filters = {}
			filters = {'item': item, 'docstatus': 1 }
			filters.update({'delivery_date': ['between',delivery_date+" and "+ return_date ]})
			
			bookings = frappe.get_all('Book Service Item', filters=filters, fields=['name', 'delivery_date', 'return_date', 'parent'])
			
			for booking in bookings:
				return "3 Already Booked: ID "+ booking.parent + " \n"+ str(filters)
			
			filters = {}
			filters = {'item': item, 'docstatus': 1 }
			filters.update({'return_date': ['between',delivery_date+" and "+ return_date]})
			
			bookings = frappe.get_all('Book Service Item', filters=filters, fields=['name', 'delivery_date', 'return_date', 'parent'])
			
			for booking in bookings:
				return "Already Booked: ID "+ booking.parent + " \n"+ str(filters)
			
			if return_date<delivery_date:
				return "Return date should be after delivery date"

		return False

@frappe.whitelist()
def make_sales_order(source_name, target_doc=None):
	cst = frappe.db.get_value("Book Service", source_name, ["customer"])
	customer = frappe.db.get_value("Customer", {"name": cst}, ["name", "customer_name"], as_dict=True)
	
	def set_missing_values(source, target):
		if customer:
			target.customer = customer.name
			target.customer_name = customer.customer_name
		target.ignore_pricing_rule = 1
		target.flags.ignore_permissions = True
		target.run_method("set_missing_values")
		target.run_method("calculate_taxes_and_totals")

	def update_item(obj, target, source_parent):
		target.stock_qty = flt(obj.quantity)

	doclist = get_mapped_doc("Book Service", source_name, {
			"Book Service": {
				"doctype": "Sales Order",
				"field_map": {
					"parent": "book_service"
				},
				"validation": {
					"docstatus": ["=", 1]
				}
			},
			"Book Service Item": {
				"doctype": "Sales Order Item",
				"field_map": {
					"service_item": "item_code"
				},
				"postprocess": update_item
			},
			"Sales Taxes and Charges": {
				"doctype": "Sales Taxes and Charges",
				"add_if_empty": True
			},
			"Sales Team": {
				"doctype": "Sales Team",
				"add_if_empty": True
			}
		}, target_doc, set_missing_values, ignore_permissions=True)

	# postprocess: fetch shipping address, set missing values

	return doclist
