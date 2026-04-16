from frappe.tests.utils import FrappeTestCase

from omnexa_agriculture.accounting_integration import ias41_adjustment_amount
from omnexa_agriculture.omnexa_agriculture.doctype.harvest_record.harvest_record import HarvestRecord


class TestHarvestRecord(FrappeTestCase):
	def test_harvest_math_fields(self):
		doc = object.__new__(HarvestRecord)
		doc.expected_yield_kg = 100
		doc.actual_yield_kg = 85
		doc.unit_price = 2
		doc.fair_value_per_kg = 2.3
		doc.seed_feed_cost = 40
		doc.fertilizer_medicine_cost = 20
		doc.labor_cost = 15
		doc.utilities_cost = 10
		doc.status = "Draft"
		doc.validate()
		self.assertEqual(doc.loss_kg, 15)
		self.assertEqual(doc.revenue_amount, 170)
		self.assertAlmostEqual(doc.ias41_fair_value_amount, 195.5, places=2)
		self.assertAlmostEqual(ias41_adjustment_amount(doc), 110.5, places=2)
