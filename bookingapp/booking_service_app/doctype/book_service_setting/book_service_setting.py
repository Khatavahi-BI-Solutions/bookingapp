# -*- coding: utf-8 -*-
# Copyright (c) 2018, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

class BookServiceSetting(Document):
	def validate(self):
		if self.enable == 1:
			setup_custom_fields()

def setup_custom_fields():
	custom_fields = {
		"Item": [
			dict(fieldname='booking_item',
			label='Booking Item',
				fieldtype='Check',
				insert_after='disabled',
				print_hide=1),
			dict(fieldname='service_item',
			label= 'Service Item',
				fieldtype='Link',
				insert_after='booking_item',
				options='Item',
				depends_on='eval:doc.booking_item',
				read_only=0, print_hide=1)
		]
	}

	create_custom_fields(custom_fields)

def make_booking_service_item(doc, method):
	book_service_setting = frappe.get_doc("Book Service Setting")
	if doc.booking_item == 1 and not doc.service_item:
		create_service_item(doc, book_service_setting)

def create_service_item(item, book_service_setting):
	service_item = frappe.new_doc("Item")
	service_item.update({
		"item_code": item.name + "_service",
		"item_group": book_service_setting.service_item_group,
		"stock_uom": book_service_setting.default_unit_of_measure,
		"is_stock_item": 0
	})
	service_item.save(ignore_permissions=True)
	frappe.db.commit()
	item.service_item = service_item.name
	item.save(ignore_permissions=True)
	frappe.db.commit()