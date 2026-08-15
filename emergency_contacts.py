import json
import os


CONTACT_FILE = "emergency_contacts.json"

def load_contacts():

    if not os.path.exists(CONTACT_FILE):

        return []

    try:

        with open(
            CONTACT_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            data = json.load(file)

        return data.get("contacts", [])

    except (json.JSONDecodeError, OSError):

        print("⚠️ Could not load emergency contacts.")
        return []
        
        
        # ==========================================
        # GET ALL ENABLED CONTACTS
        # ==========================================
        
def get_contacts():
        
            contacts = load_contacts()
        
            enabled_contacts = [
                contact
                for contact in contacts
                if contact.get("enabled", True)
            ]
        
            enabled_contacts.sort(
                key=lambda contact: contact.get(
                    "priority",
                    999
                )
            )
        
            return enabled_contacts
        
        
        # ==========================================
        # GET PRIMARY CONTACT
        # ==========================================
        
def get_contact():
        
            contacts = get_contacts()
        
            if not contacts:
        
                return None
        
            return contacts[0]
        
        
        # ==========================================
        # GET CONTACT BY NAME
        # ==========================================
        
        
        
def get_contact_by_name(name):
        
            contacts = load_contacts()
        
            for contact in contacts:
        
                if contact.get("name", "").lower() == name.lower():
        
                    return contact
        
            return None
        
        
        # ==========================================
        # DISPLAY CONTACTS
        # ==========================================
        
def display_contacts():
        
            contacts = get_contacts()
        
            print()
            print("================================")
            print("     EMERGENCY CONTACTS")
            print("================================")
        
            if not contacts:
        
                print("❌ No enabled emergency contacts.")
        
                return
        
            for contact in contacts:
        
                print(
                    f"{contact.get('priority')}. "
                    f"{contact.get('name')} → "
                    f"{contact.get('phone')}"
                )
        
            print("================================")
        
        
        # ==========================================
        # CONTACT COUNT
        # ==========================================
        
        
def get_contact_count():
        return len(get_contacts())
        