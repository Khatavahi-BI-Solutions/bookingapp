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
		if(frm.doc.docstatus == 1){
			cur_frm.add_custom_button(__('Sales Order'),
				cur_frm.cscript['Make Sales Order'], __("Make"));
			cur_frm.page.set_inner_btn_group_as_primary(__("Make"));
		}
	}
});

cur_frm.cscript['Make Sales Order'] = function() {
	frappe.model.open_mapped_doc({
		method: "bookingapp.booking_service_app.doctype.book_service.book_service.make_sales_order",
		frm: cur_frm
	})
}

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
					"fieldname": "stock_uom",
					callback: function(r) {
						get_item_price_rate(frm, cdt, cdn);
						calculate_qty(frm, cdt, cdn);
					}
				})	
			}
		})
		
	},
	delivery_date: function(frm, cdt, cdn) {
		calculate_qty(frm, cdt, cdn);
		validate_booking_date(frm, cdt, cdn, "delivery_date");
	},
	return_date: function(frm, cdt, cdn) {
		calculate_qty(frm, cdt, cdn);
		validate_booking_date(frm, cdt, cdn, "return_date");
	},
	rate: function(frm, cdt, cdn) {
		var child = locals[cdt][cdn];
		frappe.model.set_value(child.doctype, child.name, "amount", child.rate*child.quantity);
	}
})

var get_item_price_rate= function(frm, cdt, cdn) {
	var child = locals[cdt][cdn];

	frappe.model.get_value('Item Price', 
		{
			'item_code': child.service_item,
			'price_list': "Standard Selling",
			'selling': 1
		}, 
		'price_list_rate',
		function(d) {
			if(d) {
				frappe.model.set_value(child.doctype, child.name, "rate", d.price_list_rate);
			}else{
				frappe.model.set_value(child.doctype, child.name, "rate", "0");
			}
		}
	)
}

var calculate_qty= function(frm, cdt, cdn) {
	var child = locals[cdt][cdn];
	var diff = frappe.datetime.get_hour_diff(child.return_date,child.delivery_date);
	if(child.stock_uom == "Day"){
		diff = Math.ceil(diff/24);
	} 
	frappe.model.set_value(child.doctype, child.name, "quantity", diff);
	frappe.model.set_value(child.doctype, child.name, "amount", child.rate*child.quantity);
}

var validate_booking_date = function(frm, cdt, cdn,  execution_point = "") {
	frappe.call({
		"method": "validate_booking_date",
		doc: cur_frm.doc,
		callback: function (r) {
			if(r.message){
				var child = locals[cdt][cdn];
				frappe.msgprint(r.message)
				frappe.model.set_value(child.doctype, child.name, execution_point,"");
			}	
		}
	})
}