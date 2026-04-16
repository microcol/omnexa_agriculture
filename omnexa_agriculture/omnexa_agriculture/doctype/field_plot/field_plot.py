import frappe
from frappe import _
from frappe.model.document import Document


class FieldPlot(Document):
	def validate(self):
		if self.area_acre and self.area_acre <= 0:
			frappe.throw(_("Area must be greater than zero."))
