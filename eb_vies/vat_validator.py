from zeep import Client
from zeep.transports import Transport
from requests import Session
import frappe

def validate_vat_number(doc, method):
    vat_number = doc.custom_vat_number
    if not vat_number or len(vat_number) < 3:
        return  # skip empty or invalid input

    country_code = vat_number[:2].upper()
    number = vat_number[2:].replace("-", "").replace(" ", "").strip()

    try:
        session = Session()
        transport = Transport(session=session)
        client = Client(
            "http://ec.europa.eu/taxation_customs/vies/checkVatService.wsdl",
            transport=transport
        )

        result = client.service.checkVat(
            countryCode=country_code,
            vatNumber=number
        )

        if not result.valid:
            # Log the failed validation (for developers)
            frappe.log_error(f"VIES validation failed for VAT: {vat_number}")

            # Show a clean, user-friendly error in the UI
            frappe.throw(
                "The VAT number you entered is not valid according to the EU VIES database.",
                title="VIES Validation Error"
            )

    except frappe.ValidationError:
        raise  # Allow Frappe to handle expected validation errors
    except Exception as e:
        # Log unexpected API errors
        frappe.log_error(f"VIES API Error: {e}")
        frappe.throw(
            "We couldn't validate the VAT number right now due to a service issue. Please try again later.",
            title="VIES Service Unavailable"
        )
