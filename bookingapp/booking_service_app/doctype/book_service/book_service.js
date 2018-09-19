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