from frappe import _

def get_data():
    return [
        {
            "module_name": "vies",
            "type": "module",
            "label": _("EB VIES"),
            "color": "blue",
            "icon": "octicon octicon-globe",
            "category": "Modules",
            "description": "VIES VAT Validation",
        }
    ]