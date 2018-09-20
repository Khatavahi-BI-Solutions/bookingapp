// Copyright (c) 2018, Jigar Tarpara and contributors
// For license information, please see license.txt

frappe.ui.form.on('Book Service', {
	refresh: function(frm) {
		frm.set_query("item", "book_item", function(doc, cdt, cdn){
			return {
				filters: {
					"booking_item": 1
				}
			};
		});     
	}
});

frappe.ui.form.on('Book Service Item', {
	item: function(frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		cur_frm.call({
			"method": "frappe.client.get_value",
			"args": {
				"doctype": "Item",
				"filters": {
					"name":  child.item
				},
				"fieldname": "service_item"
			},
			"child": child,
			"fieldname": "service_item"
		})
		cur_frm.call({
			"method": "frappe.client.get_value",
			"args": {
				"doctype": "Item",
				"filters": {
					"name":  child.item
				},
				"fieldname": "image"
			},
			"child": child,
			"fieldname": "image"
		})
		cur_frm.call({
			"method": "frappe.client.get_value",
			"args": {
				"doctype": "Item",
				"filters": {
					"name":  child.service_item
				},
				"fieldname": "stock_uom"
			},
			"child": child,
			"fieldname": "stock_uom"
		})
		// frm.add_fetch("item", "image", "image");
		// frm.add_fetch("item", "service_item", "service_item");
		// frm.add_fetch("service_item", "stock_uom", "stock_uom");
	}
})