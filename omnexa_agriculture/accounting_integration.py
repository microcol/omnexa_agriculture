import frappe
from frappe.utils import flt


def ias41_adjustment_amount(harvest_doc) -> float:
	total_cost = (
		flt(harvest_doc.seed_feed_cost)
		+ flt(harvest_doc.fertilizer_medicine_cost)
		+ flt(harvest_doc.labor_cost)
		+ flt(harvest_doc.utilities_cost)
	)
	return flt(harvest_doc.ias41_fair_value_amount) - total_cost


def post_ias41_fair_value_journal(doc, method=None):
	"""Auto-post IAS 41 fair value adjustment for completed harvests."""
	if doc.get("status") not in ("Completed", "Sold"):
		_reverse_ias41_journal_if_any(doc)
		return
	if doc.get("ias41_journal_entry"):
		return
	if not flt(doc.get("ias41_fair_value_amount")):
		return

	farm = frappe.get_cached_doc("Farm", doc.farm)
	asset_account = farm.get("biological_asset_account")
	gain_loss_account = farm.get("ias41_gain_loss_account")
	if not asset_account or not gain_loss_account:
		return

	amount = abs(ias41_adjustment_amount(doc))
	if amount <= 0:
		return

	is_gain = ias41_adjustment_amount(doc) >= 0
	debit_account = asset_account if is_gain else gain_loss_account
	credit_account = gain_loss_account if is_gain else asset_account

	je = frappe.new_doc("Journal Entry")
	je.company = doc.company
	je.branch = doc.branch
	je.posting_date = doc.harvest_date
	je.reference = f"Harvest {doc.name}"
	je.remarks = "IAS 41 fair value adjustment from Harvest Record."
	je.append(
		"accounts",
		{
			"account": debit_account,
			"cost_center": doc.get("cost_center"),
			"project": doc.get("project"),
			"debit": amount,
			"credit": 0,
		},
	)
	je.append(
		"accounts",
		{
			"account": credit_account,
			"cost_center": doc.get("cost_center"),
			"project": doc.get("project"),
			"debit": 0,
			"credit": amount,
		},
	)
	je.insert(ignore_permissions=True)
	je.submit()

	doc.db_set("ias41_journal_entry", je.name, update_modified=False)


def _reverse_ias41_journal_if_any(doc):
	if not doc.get("ias41_journal_entry"):
		return
	if not frappe.db.exists("Journal Entry", doc.ias41_journal_entry):
		doc.db_set("ias41_journal_entry", "", update_modified=False)
		return
	je = frappe.get_doc("Journal Entry", doc.ias41_journal_entry)
	if je.docstatus == 1:
		je.cancel()
	elif je.docstatus == 0:
		je.delete(ignore_permissions=True)
	doc.db_set("ias41_journal_entry", "", update_modified=False)


