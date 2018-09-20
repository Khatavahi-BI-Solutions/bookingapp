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
			"fieldname": "image",
			callback: function(r) {
				console.log(r)
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
			}
		})
	},
	delivery_date: function(frm, cdt, cdn) {
		calculate_qty(frm, cdt, cdn);
	},
	return_date: function(frm, cdt, cdn) {
		calculate_qty(frm, cdt, cdn);
	},
})

var calculate_qty= function(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	var diff = frappe.datetime.get_hour_diff(child.return_date,child.delivery_date);
	if(child.stock_uom == "Day"){
		diff = Math.ceil(diff/24);
	} 
	frappe.model.set_value(child.doctype, child.name, "quantity", diff);
}