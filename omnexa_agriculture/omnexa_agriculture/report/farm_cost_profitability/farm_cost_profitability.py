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
		{"label": "Farm", "fieldname": "farm", "fieldtype": "Link", "options": "Farm", "width": 160},
		{"label": "Revenue", "fieldname": "revenue", "fieldtype": "Currency", "width": 120},
		{"label": "IAS 41 Fair Value", "fieldname": "ias41_fair_value", "fieldtype": "Currency", "width": 130},
		{"label": "Input Cost", "fieldname": "input_cost", "fieldtype": "Currency", "width": 130},
		{"label": "Labor Cost", "fieldname": "labor_cost", "fieldtype": "Currency", "width": 120},
		{"label": "Utilities Cost", "fieldname": "utilities_cost", "fieldtype": "Currency", "width": 120},
		{"label": "Total Cost", "fieldname": "total_cost", "fieldtype": "Currency", "width": 120},
		{"label": "IAS41 Delta", "fieldname": "ias41_delta", "fieldtype": "Currency", "width": 120},
		{"label": "Profit", "fieldname": "profit", "fieldtype": "Currency", "width": 110},
	]

	rows = frappe.get_all(
		"Harvest Record",
		fields=[
			"farm",
			"revenue_amount",
			"ias41_fair_value_amount",
			"seed_feed_cost",
			"fertilizer_medicine_cost",
			"labor_cost",
			"utilities_cost",
		],
		filters=flt_map,
		limit_page_length=2000,
	)
	agg = {}
	for row in rows:
		farm = row.get("farm")
		if farm not in agg:
			agg[farm] = {
				"farm": farm,
				"revenue": 0.0,
				"ias41_fair_value": 0.0,
				"input_cost": 0.0,
				"labor_cost": 0.0,
				"utilities_cost": 0.0,
			}
		agg[farm]["revenue"] += flt(row.get("revenue_amount"))
		agg[farm]["ias41_fair_value"] += flt(row.get("ias41_fair_value_amount"))
		agg[farm]["input_cost"] += flt(row.get("seed_feed_cost")) + flt(row.get("fertilizer_medicine_cost"))
		agg[farm]["labor_cost"] += flt(row.get("labor_cost"))
		agg[farm]["utilities_cost"] += flt(row.get("utilities_cost"))

	data = []
	for farm in sorted(agg):
		r = agg[farm]
		r["total_cost"] = r["input_cost"] + r["labor_cost"] + r["utilities_cost"]
		r["ias41_delta"] = r["ias41_fair_value"] - r["total_cost"]
		r["profit"] = r["revenue"] - r["total_cost"]
		data.append(r)
	return columns, data
