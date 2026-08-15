# ==========================================
# OMNIAI CONTACT ESCALATION ENGINE
# ==========================================

import emergency_contacts


def get_escalation_contacts():

    contacts = emergency_contacts.get_contacts()

    if not contacts:
        return []

    contacts.sort(
        key=lambda contact: contact.get(
            "priority",
            999
        )
    )

    return contacts


def get_next_contact(current_priority=None):

    contacts = get_escalation_contacts()

    if not contacts:
        return None

    if current_priority is None:
        return contacts[0]

    for contact in contacts:

        if contact.get("priority", 999) > current_priority:
            return contact

    return None


def display_escalation_plan():

    contacts = get_escalation_contacts()

    print()
    print("================================")
    print("      SOS ESCALATION PLAN")
    print("================================")

    if not contacts:

        print("❌ No emergency contacts available.")
        return

    for contact in contacts:

        print(
            f"Step {contact.get('priority', '?')}: "
            f"{contact.get('name')} → "
            f"{contact.get('phone')}"
        )

    print("================================")


def simulate_escalation():

    contacts = get_escalation_contacts()

    if not contacts:

        print("❌ No contacts configured.")
        return

    print()
    print("🚨 STARTING SOS ESCALATION")

    for contact in contacts:

        print(
            f"📞 Contacting: "
            f"{contact.get('name')} "
            f"({contact.get('phone')})"
        )

        print("📨 Emergency message prepared.")

    print("✅ Escalation simulation complete.")