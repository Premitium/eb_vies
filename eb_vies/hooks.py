app_name = "eb_vies"
app_title = "ExciseBro Vies"
app_publisher = "Simo"
app_description = "App to validate VIES numbers"
app_email = "simo@sofiaelectricbrewing.com"
app_license = "gpl-3.0"


app_icon = "octicon octicon-globe"
app_color = "blue"

# Optional:
app_version = "0.0.1"

# Link the desktop module
app_module_map = {
    "eb_vies": "eb_vies"
}

doc_events = {
    "Customer": {
        "validate": "eb_vies.vat_validator.validate_vat_number"
    }
}

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "eb_vies",
# 		"logo": "/assets/eb_vies/logo.png",
# 		"title": "ExciseBro Vies",
# 		"route": "/eb_vies",
# 		"has_permission": "eb_vies.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/eb_vies/css/eb_vies.css"
# app_include_js = "/assets/eb_vies/js/eb_vies.js"

# include js, css files in header of web template
# web_include_css = "/assets/eb_vies/css/eb_vies.css"
# web_include_js = "/assets/eb_vies/js/eb_vies.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "eb_vies/public/scss/website"

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
# app_include_icons = "eb_vies/public/icons.svg"

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
# 	"methods": "eb_vies.utils.jinja_methods",
# 	"filters": "eb_vies.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "eb_vies.install.before_install"
# after_install = "eb_vies.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "eb_vies.uninstall.before_uninstall"
# after_uninstall = "eb_vies.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "eb_vies.utils.before_app_install"
# after_app_install = "eb_vies.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "eb_vies.utils.before_app_uninstall"
# after_app_uninstall = "eb_vies.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "eb_vies.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
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

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"eb_vies.tasks.all"
# 	],
# 	"daily": [
# 		"eb_vies.tasks.daily"
# 	],
# 	"hourly": [
# 		"eb_vies.tasks.hourly"
# 	],
# 	"weekly": [
# 		"eb_vies.tasks.weekly"
# 	],
# 	"monthly": [
# 		"eb_vies.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "eb_vies.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "eb_vies.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "eb_vies.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["eb_vies.utils.before_request"]
# after_request = ["eb_vies.utils.after_request"]

# Job Events
# ----------
# before_job = ["eb_vies.utils.before_job"]
# after_job = ["eb_vies.utils.after_job"]

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
# 	"eb_vies.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

