from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("BOOKING"),
			"items": [
				{
					"type": "doctype",
					"name": "Book Service",
					"description": _("Book Service")
				},
				{
					"type": "doctype",
					"name": "Book Service Setting",
					"description": _("Book Service Setting")
				},
			]
		},
		{
			"label": _("CUSTOMER"),
			"items": [
				{
					"type": "doctype",
					"name": "Customer",
					"description": _("Customer")
				},
				{
					"type": "doctype",
					"name": "Customer Group",
					"description": _("Customer Group")
				},
				{
					"type": "doctype",
					"name": "Address",
					"description": _("Address")
				},
				{
					"type": "doctype",
					"name": "Contract",
					"description": _("Contract")
				},
				{
					"type": "doctype",
					"name": "Communication",
					"description": _("Communication")
				},
				{
					"type": "doctype",
					"name": "Appointment",
					"description": _("Appointment")
				},
				{
					"type": "doctype",
					"name": "Newsletter",
					"description": _("Newsletter")
				},
				{
					"type": "doctype",
					"name": "Email Group",
					"description": _("Email Group")
				},
			]
		},
		{
			"label": _("SELLING CYCLE"),
			"items": [
				{
					"type": "doctype",
					"name": "Quotation",
					"description": _("Quotation")
				},
				{
					"type": "doctype",
					"name": "Sales Order",
					"description": _("Sales Order")
				},
				{
					"type": "doctype",
					"name": "Sales Invoice",
					"description": _("Sales Invoice")
				},
				{
					"type": "doctype",
					"name": "Blanket Order",
					"description": _("Blanket Order")
				},
				{
					"type": "doctype",
					"name": "Sales Partner",
					"description": _("Sales Partner")
				},
				{
					"type": "doctype",
					"name": "Sales Person Tree",
					"description": _("Sales Person Tree")
				},
				{
					"type": "doctype",
					"name": "Sales Taxes and Charges Template",
					"description": _("CustSales Taxes and Charges Templateomer")
				},
			]
		}, 
		{
			"label": _("STOCK TRANSACTION"),
			"items": [
				{
					"type": "doctype",
					"name": "Stock Entry",
					"description": _("Stock Entry")
				},
				{
					"type": "doctype",
					"name": "Delivery Note",
					"description": _("Delivery Note")
				},
				{
					"type": "doctype",
					"name": "Warehouse",
					"description": _("Warehouse")
				},
				{
					"type": "doctype",
					"name": "Material Request",
					"description": _("Material Request")
				},
			]
		},
		{
			"label": _("ITEMS AND PRICING"),
			"items": [
				{
					"type": "doctype",
					"name": "Item",
					"description": _("Item")
				},
				{
					"type": "doctype",
					"name": "Price List",
					"description": _("Price List")
				},
				{
					"type": "doctype",
					"name": "Item Price",
					"description": _("Item Price")
				},
				{
					"type": "doctype",
					"name": "Shipping Rule",
					"description": _("Shipping Rule")
				},
				{
					"type": "doctype",
					"name": "Pricing Rule",
					"description": _("Pricing Rule")
				},
				{
					"type": "doctype",
					"name": "Serial No",
					"description": _("Serial No")
				},
				{
					"type": "doctype",
					"name": "Batch",
					"description": _("Batch")
				},
				{
					"type": "doctype",
					"name": "Coupon Code",
					"description": _("Coupon Code")
				},
			]
		},
		{
			"label": _("SUPPORT"),
			"items": [
				
				{
					"type": "doctype",
					"name": "Issue",
					"description": _("Issue")
				},
				{
					"type": "doctype",
					"name": "Warranty Claim",
					"description": _("Warranty Claim")
				},
				{
					"type": "doctype",
					"name": "Issue Type",
					"description": _("Issue Type")
				},
				{
					"type": "doctype",
					"name": "Issue Priority",
					"description": _("Issue Priority")
				},
				{
					"type": "doctype",
					"name": "Service Level",
					"description": _("Service Level")
				},
				{
					"type": "doctype",
					"name": "Service Level Agreement",
					"description": _("Service Level Agreement")
				},
				{
					"type": "doctype",
					"name": "Support Settings",
					"description": _("Support Settings")
				},
			]
		}, 
		{
			"label": _("SETTING"),
			"items": [
				{
					"type": "doctype",
					"name": "Stock Settings",
					"description": _("Stock Settings")	
				},
				{
					"type": "doctype",
					"name": "UOM",
					"description": _("UOM")	
				},
				{
					"type": "doctype",
					"name": "Item Attribute",
					"description": _("Item Attribute")	
				},
				{
					"type": "doctype",
					"name": "Terms and Conditions",
					"description": _("Terms and Conditions")
				},
				{
					"type": "doctype",
					"name": "Selling Settings",
					"description": _("Selling Settings")	
				},
				{
					"type": "doctype",
					"name": "SMS Center",
					"description": _("SMS Center")	
				},
				{
					"type": "doctype",
					"name": "SMS Log",
					"description": _("SMS Log")	
				},
				{
					"type": "doctype",
					"name": "SMS Settings",
					"description": _("SMS Settings")	
				},
				{
					"type": "doctype",
					"name": "Mode of Payment",
					"description": _("Mode of Payment")	
				},
				{
					"type": "doctype",
					"name": "Currency",
					"description": _("Currency")	
				},
			]
		},
		{
			"label": _("ACCOUNTING"),
			"items": [
				{
					"type": "doctype",
					"name": "Tax Category",
					"description": _("Tax Category")
				},
				{
					"type": "doctype",
					"name": "Tax Rule",
					"description": _("Tax Rule")
				},
				{
					"type": "doctype",
					"name": "Item Tax Template",
					"description": _("Item Tax Template")
				},
				{
					"type": "doctype",
					"name": "Payment Entry",
					"description": _("Payment Entry")
				},
				{
					"type": "doctype",
					"name": "Payment Request",
					"description": _("Payment Request")
				},
				{
					"type": "report",
					"name": "Accounts Receivable",
					"description": _("Accounts Receivable"),
					"is_query_report": True,
					"reference_doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"name": "Ordered Items To Be Billed",
					"description": _("Ordered Items To Be Billed"),
					"is_query_report": True,
					"reference_doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"name": "Delivered Items To Be Billed",
					"description": _("Delivered Items To Be Billed"),
					"is_query_report": True,
					"reference_doctype": "Sales Invoice",
				},
				{
					"type": "doctype",
					"name": "Accounts Settings",
					"description": _("Accounts Settings")
				},
				{
					"type": "doctype",
					"name": "Fiscal Year",
					"description": _("Fiscal Year")
				},
				{
					"type": "doctype",
					"name": "Accounting Period",
					"description": _("Accounting Period")
				},
				{
					"type": "doctype",
					"name": "Payment Term",
					"description": _("Payment Term")
				},
			]
		},
		{
			"label": _("KEY REPORTS"),
			"items": [
				{
					"type": "report",
					"name": "Trial Balance",
					"description": _("Trial Balance"),
					"is_query_report": True,
					"reference_doctype": "GL Entry",
				},
				{
					"type": "report",
					"name": "Sales Analytics",
					"description": _("Sales Analytics"),
					"is_query_report": True,
					"reference_doctype": "Sales Order",
				},
				{
					"type": "report",
					"name": "Profitability Analysis",
					"description": _("Profitability Analysis"),
					"is_query_report": True,
					"reference_doctype": "GL Entry",
				},
				{
					"type": "doctype",
					"name": "Quick Stock Balance",
					"description": _("Quick Stock Balance")
				},
			]
		},
		{
			"label": _("STOCKS REPORT"),
			"items": [
				{
					"type": "report",
					"name": "Customers Without Any Sales Transactions",
					"description": _("Customers Without Any Sales Transactions"),
					"is_query_report": True,
					"reference_doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"name": "Customer Ledger Summary",
					"description": _("Customer Ledger Summary"),
					"is_query_report": True,
					"reference_doctype": "Sales Invoice",
				},
				{
					"type": "report",
					"name": "Stock Balance",
					"description": _("Stock Balance"),
					"is_query_report": True,
					"reference_doctype": "Stock Ledger Entry",
				},
				{
					"type": "doctype",
					"name": "Stock Reconciliation",
					"description": _("Stock Reconciliation")
				},
				{
					"type": "report",
					"name": "Supplier Ledger Summary",
					"description": _("Supplier Ledger Summary"),
					"is_query_report": True,
					"reference_doctype": "Purchase Invoice",
				},
				{
					"type": "report",
					"name": "Profit and Loss Statement",
					"description": _("Profit and Loss Statement"),
					"is_query_report": True,
					"reference_doctype": "GL Entry",
				},
			]
		},
		{
			"label": _("OVERALL REPORTS"),
			"items": [
				{
					"type": "report",
					"name": "Item-wise Sales History",
					"description": _("Item-wise Sales History"),
					"is_query_report": True,
					"reference_doctype": "Sales Order",
				},
				{
					"type": "report",
					"name": "Balance Sheet",
					"description": _("Balance Sheet"),
					"is_query_report": True,
					"reference_doctype": "GL Entry",
				},
				{
					"type": "report",
					"name": "Sales Person-wise Transaction Summary",
					"description": _("Sales Person-wise Transaction Summary"),
					"is_query_report": True,
					"reference_doctype": "Sales Order",
				},
				{
					"type": "report",
					"name": "Delivery Note Trends",
					"description": _("Delivery Note Trends"),
					"is_query_report": True,
					"reference_doctype": "Delivery Note",
				},
				{
					"type": "report",
					"name": "Cash Flow",
					"description": _("Cash Flow"),
					"is_query_report": True,
					"reference_doctype": "GL Entry",
				},
			]
		}
    ]