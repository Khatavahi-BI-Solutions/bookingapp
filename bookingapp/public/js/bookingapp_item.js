frappe.ui.form.on('Item', {
    booking_item: function(frm) {
        if(frm.doc.booking_item == 0){
            frm.doc.service_item = ""
        }
    }
})