import frappe
from frappe.utils import getdate, nowdate


def execute(filters=None):
	filters = filters or {}
	flt_map = {"docstatus": ["<", 2]}
	if filters.get("farm"):
		flt_map["farm"] = filters["farm"]
	if filters.get("branch"):
		flt_map["branch"] = filters["branch"]

	columns = [
		{"label": "Record", "fieldname": "name", "fieldtype": "Link", "options": "Vaccination Record", "width": 140},
		{"label": "Farm", "fieldname": "farm", "fieldtype": "Link", "options": "Farm", "width": 140},
		{"label": "Animal", "fieldname": "animal", "fieldtype": "Link", "options": "Livestock Animal", "width": 140},
		{"label": "Vaccine", "fieldname": "vaccine_name", "fieldtype": "Data", "width": 170},
		{"label": "Administered", "fieldname": "administered_on", "fieldtype": "Date", "width": 110},
		{"label": "Next Due", "fieldname": "next_due_date", "fieldtype": "Date", "width": 110},
		{"label": "Current Status", "fieldname": "current_status", "fieldtype": "Data", "width": 110},
	]

	data = frappe.get_all(
		"Vaccination Record",
		fields=["name", "farm", "animal", "vaccine_name", "administered_on", "next_due_date"],
		filters=flt_map,
		order_by="next_due_date asc, modified desc",
		limit_page_length=1000,
	)
	today = getdate(nowdate())
	for row in data:
		if not row.get("next_due_date"):
			row["current_status"] = "Completed"
		elif getdate(row["next_due_date"]) < today:
			row["current_status"] = "Overdue"
		else:
			row["current_status"] = "Due Soon"
	return columns, data
