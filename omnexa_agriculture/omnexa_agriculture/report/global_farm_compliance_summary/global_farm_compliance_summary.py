import frappe
from frappe.utils import getdate, nowdate


def execute(filters=None):
	filters = filters or {}
	flt_map = {"docstatus": ["<", 2]}
	if filters.get("company"):
		flt_map["company"] = filters["company"]
	if filters.get("branch"):
		flt_map["branch"] = filters["branch"]

	columns = [
		{"label": "Farm", "fieldname": "name", "fieldtype": "Link", "options": "Farm", "width": 140},
		{"label": "Farm Name", "fieldname": "farm_name", "fieldtype": "Data", "width": 160},
		{"label": "Country", "fieldname": "country", "fieldtype": "Link", "options": "Country", "width": 100},
		{"label": "Timezone", "fieldname": "timezone", "fieldtype": "Data", "width": 120},
		{"label": "Currency", "fieldname": "operating_currency", "fieldtype": "Link", "options": "Currency", "width": 95},
		{"label": "IAS 41 Method", "fieldname": "ifrs_valuation_method", "fieldtype": "Data", "width": 170},
		{"label": "GlobalG.A.P Cert", "fieldname": "global_gap_cert_no", "fieldtype": "Data", "width": 140},
		{"label": "Valid Until", "fieldname": "global_gap_valid_until", "fieldtype": "Date", "width": 95},
		{"label": "Compliance Status", "fieldname": "compliance_status", "fieldtype": "Data", "width": 120},
	]

	data = frappe.get_all(
		"Farm",
		fields=[
			"name",
			"farm_name",
			"country",
			"timezone",
			"operating_currency",
			"ifrs_valuation_method",
			"global_gap_cert_no",
			"global_gap_valid_until",
		],
		filters=flt_map,
		order_by="farm_name asc",
		limit_page_length=1000,
	)
	today = getdate(nowdate())
	for row in data:
		if not row.get("global_gap_cert_no"):
			row["compliance_status"] = "Missing Cert"
		elif row.get("global_gap_valid_until") and getdate(row["global_gap_valid_until"]) < today:
			row["compliance_status"] = "Expired"
		else:
			row["compliance_status"] = "Active"
	return columns, data
