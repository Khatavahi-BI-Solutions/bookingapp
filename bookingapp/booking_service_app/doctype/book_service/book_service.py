# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class BookService(Document):
	def validate_booking_date(self,child):
		# self.delivery_date
		# self.return_date
		# print(self.delivery_date)
		# print(self.return_date)
		for row in self.book_item:
			print(row.delivery_date)
			print(row.return_date)
		return True
