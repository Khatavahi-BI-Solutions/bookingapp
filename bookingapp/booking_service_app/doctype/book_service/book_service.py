# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
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

		return False