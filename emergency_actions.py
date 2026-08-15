# ==========================================
# OMNIAI EMERGENCY ACTION MANAGER
# ==========================================

import re
import webbrowser
import sms_gateway
import contact_escalation


# Keep this as "DEMO" while testing.
#
# Change to "OPEN_CALL_APP" only after you have configured
# a calling application on Windows that supports tel: links.
CALL_MODE = "DEMO"


def clean_phone_number(phone):
    """
    Keeps only digits and a leading +.
    Prevents malformed number strings from being opened.
    """
    phone = str(phone).strip()

    if phone.startswith("+"):
        return "+" + re.sub(r"\D", "", phone[1:])

    return re.sub(r"\D", "", phone)


def prepare_call(contact):
    if not contact:
        return {
            "status": "FAILED",
            "action": "CALL",
            "message": "No contact is available."
        }

    name = contact.get("name", "Unknown")
    phone = clean_phone_number(contact.get("phone", ""))

    if not phone:
        return {
            "status": "FAILED",
            "action": "CALL",
            "contact": name,
            "message": "This contact has no valid phone number."
        }

    if CALL_MODE == "DEMO":
        print()
        print("📞 DEMO CALL")
        print("Contact:", name)
        print("Number:", phone)

        return {
            "status": "PREPARED",
            "action": "CALL",
            "contact": name,
            "phone": phone,
            "message": f"Demo call prepared for {name}."
        }

    if CALL_MODE == "OPEN_CALL_APP":
        try:
            # Opens the user's configured phone/calling application.
            # This does not bypass Windows or carrier confirmation.
            opened = webbrowser.open(f"tel:{phone}")

            if opened:
                print(f"📞 Call application opened for {name}: {phone}")

                return {
                    "status": "CALL_APP_OPENED",
                    "action": "CALL",
                    "contact": name,
                    "phone": phone,
                    "message": f"Calling application opened for {name}."
                }

            return {
                "status": "FAILED",
                "action": "CALL",
                "contact": name,
                "phone": phone,
                "message": "No Windows calling application could be opened."
            }

        except Exception as error:
            return {
                "status": "FAILED",
                "action": "CALL",
                "contact": name,
                "phone": phone,
                "message": f"Could not open calling application: {error}"
            }

    return {
        "status": "FAILED",
        "action": "CALL",
        "contact": name,
        "phone": phone,
        "message": "Invalid CALL_MODE setting."
    }


def prepare_message(contact, sos_message):
    if not contact:
        return {
            "status": "FAILED",
            "action": "MESSAGE",
            "message": "No contact is available."
        }

    name = contact.get("name", "Unknown")
    phone = clean_phone_number(contact.get("phone", ""))

    print()
    print("📨 SOS MESSAGE PREPARED")
    print("To:", name)
    print("Number:", phone)
    print(sos_message)

    return sms_gateway.send_sms(contact, sos_message)


def prepare_emergency_action(sos_message):
    contacts = contact_escalation.get_escalation_contacts()

    if not contacts:
        return {
            "status": "FAILED",
            "message": "No emergency contacts are configured.",
            "actions": []
        }

    actions = []

    for contact in contacts:
        call_result = prepare_call(contact)
        message_result = prepare_message(contact, sos_message)

        actions.append({
            "contact": contact.get("name", "Unknown"),
            "phone": contact.get("phone", "Unknown"),
            "call": call_result,
            "message": message_result
        })

    return {
        "status": "PREPARED",
        "message": "Emergency contact actions prepared.",
        "actions": actions
    }