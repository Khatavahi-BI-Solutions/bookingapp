import frappe

def make_booking_service_item(doc, method):
	book_service_setting = frappe.get_doc("Book Service Setting")
	if doc.booking_item == 1 and not doc.service_item:
		create_service_item(doc, book_service_setting)

def create_service_item(item, book_service_setting):
    if not frappe.db.exists("Item", item.name + "_service"):
        service_item = frappe.new_doc("Item")
        service_item.update({
            "item_code": item.name + "_service",
            "item_group": book_service_setting.service_item_group,
            "stock_uom": book_service_setting.default_unit_of_measure,
            "is_stock_item": 0
        })
        service_item.save(ignore_permissions=True)
        item.service_item = service_item.name
        item.save(ignore_permissions=True)
    else:
        item.service_item = item.name + "_service"
        item.save(ignore_permissions=True)
    frappe.db.commit()
    