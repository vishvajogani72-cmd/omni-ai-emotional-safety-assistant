import emergency_contacts


print("Testing emergency contacts...")

contacts = emergency_contacts.get_contacts()

print()
print("Total enabled contacts:", len(contacts))

for contact in contacts:

    print(
        contact["priority"],
        contact["name"],
        contact["phone"]
    )


print()

primary = emergency_contacts.get_contact()

if primary:

    print("⭐ Primary contact:")
    print(primary["name"])
    print(primary["phone"])

else:

    print("❌ No primary contact found")


print()

emergency_contacts.display_contacts()