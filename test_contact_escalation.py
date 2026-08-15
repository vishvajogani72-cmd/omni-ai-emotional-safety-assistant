import contact_escalation


contact_escalation.display_escalation_plan()

print()

first = contact_escalation.get_next_contact()

if first:

    print("⭐ First contact:")
    print(first["name"])
    print(first["phone"])

    next_contact = contact_escalation.get_next_contact(
        first["priority"]
    )

    if next_contact:

        print()
        print("➡️ Next contact:")
        print(next_contact["name"])
        print(next_contact["phone"])

print()

contact_escalation.simulate_escalation()