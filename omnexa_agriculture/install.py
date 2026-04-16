import frappe


def _ensure_roles():
	for role_name in (
		"Farm Manager",
		"Veterinarian",
		"Farm Worker",
		"Agriculture Accountant",
	):
		if frappe.db.exists("Role", role_name):
			continue
		role = frappe.new_doc("Role")
		role.role_name = role_name
		role.desk_access = 1
		role.insert(ignore_permissions=True)


def after_install():
	_ensure_roles()


def after_migrate():
	_ensure_roles()
