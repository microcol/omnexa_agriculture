import frappe
from frappe import _
from frappe.model.document import Document


class VaccinationRecord(Document):
	def validate(self):
		if self.next_due_date and self.administered_on and self.next_due_date < self.administered_on:
			frappe.throw(_("Next Due Date cannot be before Administered On date."))
