import frappe
from frappe import _
from frappe.model.document import Document
from frappe.utils import flt


class HarvestRecord(Document):
	def validate(self):
		self.loss_kg = max(0, flt(self.expected_yield_kg) - flt(self.actual_yield_kg))
		self.revenue_amount = flt(self.actual_yield_kg) * flt(self.unit_price)
		self.ias41_fair_value_amount = flt(self.actual_yield_kg) * flt(self.fair_value_per_kg)
		self._validate_ias41_setup()

	def _validate_ias41_setup(self):
		if self.status not in ("Completed", "Sold"):
			return
		if not self.farm:
			return
		farm = frappe.get_cached_doc("Farm", self.farm)
		if not farm.get("biological_asset_account") or not farm.get("ias41_gain_loss_account"):
			frappe.throw(
				_(
					"Farm {0} is missing IAS 41 accounts. Set Biological Asset Account and IAS 41 Gain/Loss Account before closing harvest."
				).format(self.farm),
				title=_("IAS 41 Setup Required"),
			)
