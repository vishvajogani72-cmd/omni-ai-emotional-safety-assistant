import time
import location_ai


# ======================================
# EMERGENCY MODE
# ======================================

emergency_active = False


def activate_emergency():

    global emergency_active

    emergency_active = True

    print("\n🚨 EMERGENCY MODE ACTIVATED")
    print("⚠️ Stay calm, Owner.")
    print("⏳ SOS countdown starting...")

    # Safe testing countdown
    for seconds in range(5, 0, -1):

        print(f"🚨 SOS in {seconds}...")
        time.sleep(1)

    print("📢 TEST SOS TRIGGERED")
    # cature loacation
    location=location_ai.get_location()
    print(f" 📍 Location: "
          f"{location['latitude']},"
          f"{location['longitude']}")

    print("📞 Emergency contact action would happen here.")

    return (
        "Emergency mode activated, Owner. "
        f"Your test location is"
        f"{location['latitude']},"
        f"{location['longitude']}."
    )


def cancel_emergency():

    global emergency_active

    emergency_active = False
    print("✅ Emergency mode cancelled.")

    return (
        "Emergency mode cancelled, Owner."
    )