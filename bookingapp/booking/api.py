from .endpoints.get_weekly_report import GetWeeklyReport
from frappe import whitelist


@whitelist()
def get_weekly_report():
    return GetWeeklyReport().run()
