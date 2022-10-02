frappe.views.calendar['Book Service'] = {
	field_map: {
		start: 'from_time',
		end: 'to_time',
		id: 'name',
		allDay: 'allDay',
		title: 'subject',
		// status: 'event_type',
		color: 'color'
	},
	gantt: true,
	style_map: {
		Public: 'success',
		Private: 'info'
	},
	// order_by: 'to_time',
	get_events_method: 'bookingapp.booking_service_app.doctype.book_service.book_service.get_book_service_details'
}