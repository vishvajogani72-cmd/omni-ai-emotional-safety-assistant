import safety_engine
from datetime import datetime
import location_ai
import emergency_contacts
from datetime import datetime

def generate_sos_message(
    emergency_type="Emergency",
    risk_level="CRITICAL",
    risk_score=100,
    risk_reason="Emergency detected"
):

    # Get location
    location = location_ai.get_location()
   
    latitude = location.get("latitude", "Unknown")
    longitude = location.get("longitude", "Unknown")
    place = location.get("place", "Unknown")
    maps_link = location.get("maps_link", "")
    location_mode = location.get("mode", "Unknown")
   

    # Get emergency contact
    try:
        contacts = emergency_contacts.get_contacts()
    except AttributeError:
        contact = emergency_contacts.get_contact()
        contacts = [contact] if contact else []
    if contacts:
            contact_lines = []
    
            for contact in contacts:
                name = contact.get("name", "Emergency Contact")
                phone = contact.get("phone", "Unknown number")
    
                contact_lines.append(f"👤 {name}: {phone}")
    
            contact_text = "\n".join(contact_lines)
    
    else:
            contact_text = "No emergency contacts configured."
    
            current_time = datetime.now().strftime(
            "%d %B %Y, %I:%M %p"
        )
    

    # ======================================
    # BUILD MESSAGE
    # ======================================

    message = (
        "\n"
        "================================\n"
        "       🚨 OMNI SAFE ALERT\n"
        "================================\n\n"

        f"🚨 Emergency Type: {emergency_type}\n"
        f"⚠️ Risk Level: {risk_level}\n"
        f"📊 Risk Score: {risk_score}/100\n"
        f"🧠 Reason: {risk_reason}\n\n"

        f"👤 Contact: {contact_text}\n"
        f"🕐 Time: {current_time}\n\n"

        "Please contact me immediately.\n"

        "================================\n"
    )

    return message.strip()