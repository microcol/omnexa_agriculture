from omnexa_core.omnexa_core.branch_access import (
	enforce_branch_access,
	permission_query_conditions_for_branch_field,
)
from omnexa_core.omnexa_core.user_context import apply_company_branch_defaults


def enforce_branch_access_for_doc(doc, method=None):
	enforce_branch_access(doc)


def populate_company_branch_from_user_context(doc, method=None):
	apply_company_branch_defaults(doc)


def farm_query_conditions(user=None):
	return permission_query_conditions_for_branch_field("Farm", user)


def field_plot_query_conditions(user=None):
	return permission_query_conditions_for_branch_field("Field Plot", user)


def crop_cycle_query_conditions(user=None):
	return permission_query_conditions_for_branch_field("Crop Cycle", user)


def livestock_animal_query_conditions(user=None):
	return permission_query_conditions_for_branch_field("Livestock Animal", user)


def vaccination_record_query_conditions(user=None):
	return permission_query_conditions_for_branch_field("Vaccination Record", user)


def harvest_record_query_conditions(user=None):
	return permission_query_conditions_for_branch_field("Harvest Record", user)
