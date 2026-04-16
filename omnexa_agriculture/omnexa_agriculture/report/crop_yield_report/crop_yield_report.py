import frappe
from frappe.utils import flt


def execute(filters=None):
	filters = filters or {}
	flt_map = {"docstatus": ["<", 2]}
	if filters.get("farm"):
		flt_map["farm"] = filters["farm"]
	if filters.get("branch"):
		flt_map["branch"] = filters["branch"]

	columns = [
		{"label": "Harvest", "fieldname": "name", "fieldtype": "Link", "options": "Harvest Record", "width": 140},
		{"label": "Farm", "fieldname": "farm", "fieldtype": "Link", "options": "Farm", "width": 140},
		{"label": "Crop Cycle", "fieldname": "crop_cycle", "fieldtype": "Link", "options": "Crop Cycle", "width": 140},
		{"label": "Expected Kg", "fieldname": "expected_yield_kg", "fieldtype": "Float", "width": 110},
		{"label": "Actual Kg", "fieldname": "actual_yield_kg", "fieldtype": "Float", "width": 110},
		{"label": "Loss Kg", "fieldname": "loss_kg", "fieldtype": "Float", "width": 110},
		{"label": "Loss %", "fieldname": "loss_pct", "fieldtype": "Percent", "width": 90},
	]

	data = frappe.get_all(
		"Harvest Record",
		fields=["name", "farm", "crop_cycle", "expected_yield_kg", "actual_yield_kg", "loss_kg"],
		filters=flt_map,
		order_by="modified desc",
		limit_page_length=1000,
	)
	for row in data:
		expected = flt(row.get("expected_yield_kg"))
		row["loss_pct"] = (flt(row.get("loss_kg")) / expected * 100) if expected else 0
	return columns, data
