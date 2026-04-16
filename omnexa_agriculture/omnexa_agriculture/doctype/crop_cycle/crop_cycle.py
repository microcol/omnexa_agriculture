import frappe
from frappe import _
from frappe.model.document import Document


class CropCycle(Document):
	def validate(self):
		if self.expected_yield_kg and self.expected_yield_kg < 0:
			frappe.throw(_("Expected yield cannot be negative."))
