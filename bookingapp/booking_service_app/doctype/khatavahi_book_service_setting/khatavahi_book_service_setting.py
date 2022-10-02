# -*- coding: utf-8 -*-
# Copyright (c) 2019, Jigar Tarpara and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields


class KhatavahiBookServiceSetting(Document):

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
                 label='Service Item',
                 fieldtype='Link',
                 insert_after='booking_item',
                 options='Item',
                 depends_on='eval:doc.booking_item',
                 read_only=0, print_hide=1)
        ],
        "Sales Order": [
            dict(fieldname='book_service',
                 label='Book Service',
                 fieldtype='Link',
                 insert_after='customer_name',
                 read_only=0,
                 options='Book Service'
                 ),
        ]
    }

    create_custom_fields(custom_fields)
    frappe.msgprint("Custom Field Updated!")
