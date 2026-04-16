app_name = "omnexa_agriculture"
app_title = "ErpGenEx — Agriculture"
app_publisher = "Omnexa"
app_description = "Agriculture vertical"
app_email = "dev@omnexa.com"
app_license = "mit"

# Apps
# ------------------

required_apps = ["omnexa_core", "omnexa_accounting", "omnexa_hr", "omnexa_services"]

# Each item in the list will be shown as an app in the apps page
add_to_apps_screen = [
	{
		"name": "omnexa_agriculture",
		"logo": "/assets/omnexa_agriculture/agriculture.svg",
		"title": "Agriculture",
		"route": "/app/agriculture",
	}
]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/omnexa_agriculture/css/omnexa_agriculture.css"
# app_include_js = "/assets/omnexa_agriculture/js/omnexa_agriculture.js"

# include js, css files in header of web template
# web_include_css = "/assets/omnexa_agriculture/css/omnexa_agriculture.css"
# web_include_js = "/assets/omnexa_agriculture/js/omnexa_agriculture.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "omnexa_agriculture/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "omnexa_agriculture/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "omnexa_agriculture.utils.jinja_methods",
# 	"filters": "omnexa_agriculture.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "omnexa_agriculture.install.before_install"
after_install = "omnexa_agriculture.install.after_install"
after_migrate = ["omnexa_agriculture.install.after_migrate"]

# Uninstallation
# ------------

# before_uninstall = "omnexa_agriculture.uninstall.before_uninstall"
# after_uninstall = "omnexa_agriculture.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "omnexa_agriculture.utils.before_app_install"
# after_app_install = "omnexa_agriculture.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "omnexa_agriculture.utils.before_app_uninstall"
# after_app_uninstall = "omnexa_agriculture.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "omnexa_agriculture.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

permission_query_conditions = {
	"Farm": "omnexa_agriculture.permissions.farm_query_conditions",
	"Field Plot": "omnexa_agriculture.permissions.field_plot_query_conditions",
	"Crop Cycle": "omnexa_agriculture.permissions.crop_cycle_query_conditions",
	"Livestock Animal": "omnexa_agriculture.permissions.livestock_animal_query_conditions",
	"Vaccination Record": "omnexa_agriculture.permissions.vaccination_record_query_conditions",
	"Harvest Record": "omnexa_agriculture.permissions.harvest_record_query_conditions",
}
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Farm": {
		"before_validate": "omnexa_agriculture.permissions.populate_company_branch_from_user_context",
		"validate": "omnexa_agriculture.permissions.enforce_branch_access_for_doc",
	},
	"Field Plot": {
		"before_validate": "omnexa_agriculture.permissions.populate_company_branch_from_user_context",
		"validate": "omnexa_agriculture.permissions.enforce_branch_access_for_doc",
	},
	"Crop Cycle": {
		"before_validate": "omnexa_agriculture.permissions.populate_company_branch_from_user_context",
		"validate": "omnexa_agriculture.permissions.enforce_branch_access_for_doc",
	},
	"Livestock Animal": {
		"before_validate": "omnexa_agriculture.permissions.populate_company_branch_from_user_context",
		"validate": "omnexa_agriculture.permissions.enforce_branch_access_for_doc",
	},
	"Vaccination Record": {
		"before_validate": "omnexa_agriculture.permissions.populate_company_branch_from_user_context",
		"validate": "omnexa_agriculture.permissions.enforce_branch_access_for_doc",
	},
	"Harvest Record": {
		"before_validate": "omnexa_agriculture.permissions.populate_company_branch_from_user_context",
		"validate": "omnexa_agriculture.permissions.enforce_branch_access_for_doc",
		"on_update": "omnexa_agriculture.accounting_integration.post_ias41_fair_value_journal",
	},
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"omnexa_agriculture.tasks.all"
# 	],
# 	"daily": [
# 		"omnexa_agriculture.tasks.daily"
# 	],
# 	"hourly": [
# 		"omnexa_agriculture.tasks.hourly"
# 	],
# 	"weekly": [
# 		"omnexa_agriculture.tasks.weekly"
# 	],
# 	"monthly": [
# 		"omnexa_agriculture.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "omnexa_agriculture.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "omnexa_agriculture.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "omnexa_agriculture.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
before_request = ["omnexa_agriculture.license_gate.before_request"]
# after_request = ["omnexa_agriculture.utils.after_request"]

# Job Events
# ----------
# before_job = ["omnexa_agriculture.utils.before_job"]
# after_job = ["omnexa_agriculture.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"omnexa_agriculture.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

