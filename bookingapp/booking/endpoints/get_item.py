from client_customizer.utils import ApiEndpoint
import frappe
from frappe.utils.data import get_url


class GetWeeklyReport(ApiEndpoint):
    def __init__(self):
        super(GetWeeklyReport, self).__init__("Get Weekly Report API")

    def default(self, *args, **kwargs):
        valid, response = self.validate_required_parameters(kwargs, [
                                                            "user_id"])
        if not valid:
            return response

        user_id = kwargs.get("user_id")

        if not user_id:
            return self.respond_with_code(code=401, error_code="Unauthorized")

        user_roles = frappe.get_roles(user_id)

        if "Student" not in user_roles:
            return self.respond_with_code(code=401, error_code="Unauthorized")

        if not frappe.db.exists("User", user_id):
            return self.respond_with_code(code=404, error_code="UserNotFound")

        if not frappe.db.exists("Students", {"user_id": user_id}):
            return self.respond_with_code(code=404, error_code="StudentNotFound")

        student = frappe.get_doc("Students", {"user_id": user_id})

        subscriptions = student.subscriptions

        quizes = []
        for s in subscriptions:
            subscription = frappe.get_doc("Subscriptions", s.subscription)
            for q in subscription.shown_quizzes:
                quizes.append(q.quiz)

        context = []
        for row in set(quizes):
            context.append({
                "id": row,
                "title": frappe.get_value("Quizzes", row, "quiz_name"),
                "image": self.get_image_url(frappe.get_value("Quizzes", row, "image"))
            })

        return self.respond_with_code(data={"quizzes": context})

    def get_image_url(self, img):
        return get_url() + img if img else None
