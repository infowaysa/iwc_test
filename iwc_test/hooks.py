app_name = "iwc_test"
app_title = "IWC Test"
app_publisher = "InfoWay for ICT"
app_description = "This is a test app"
app_email = "support@infoway.com.sa"
app_license = "MIT"

# Includes in <head>
# ------------------
fixtures = [
    "Custom Field",
    "Print Format",
    "Custom DocPerm",
    # Add any other DocTypes or records you've customized.
]
# include js, css files in header of desk.html
# app_include_css = "/assets/iwc_test/css/iwc_test.css"
# app_include_js = "/assets/iwc_test/js/iwc_test.js"

# include js, css files in header of web template
# web_include_css = "/assets/iwc_test/css/iwc_test.css"
# web_include_js = "/assets/iwc_test/js/iwc_test.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "iwc_test/public/scss/website"

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
# 	"methods": "iwc_test.utils.jinja_methods",
# 	"filters": "iwc_test.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "iwc_test.install.before_install"
# after_install = "iwc_test.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "iwc_test.uninstall.before_uninstall"
# after_uninstall = "iwc_test.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "iwc_test.utils.before_app_install"
# after_app_install = "iwc_test.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "iwc_test.utils.before_app_uninstall"
# after_app_uninstall = "iwc_test.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iwc_test.notifications.get_notification_config"

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
# 		"iwc_test.tasks.all"
# 	],
# 	"daily": [
# 		"iwc_test.tasks.daily"
# 	],
# 	"hourly": [
# 		"iwc_test.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iwc_test.tasks.weekly"
# 	],
# 	"monthly": [
# 		"iwc_test.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "iwc_test.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "iwc_test.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "iwc_test.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["iwc_test.utils.before_request"]
# after_request = ["iwc_test.utils.after_request"]

# Job Events
# ----------
# before_job = ["iwc_test.utils.before_job"]
# after_job = ["iwc_test.utils.after_job"]

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
# 	"iwc_test.auth.validate"
# ]
