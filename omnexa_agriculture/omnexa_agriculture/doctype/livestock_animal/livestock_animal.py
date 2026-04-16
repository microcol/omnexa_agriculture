import frappe
from frappe import _
from frappe.model.document import Document


class LivestockAnimal(Document):
	def validate(self):
		if not self.birth_date and not self.purchase_date:
			frappe.throw(_("Set either Birth Date or Purchase Date."))
