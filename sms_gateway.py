import re
import time
import serial


# ==========================================
# GSM MODEM SETTINGS
# ==========================================

# Change COM3 after checking Device Manager.
MODEM_PORT = "COM3"
BAUD_RATE = 115200

# Keep DEMO while testing.
# Change to GSM_MODEM only after your USB GSM modem and SIM work.
SMS_MODE = "DEMO"


def clean_phone_number(phone):
    phone = str(phone).strip()

    if phone.startswith("+"):
        return "+" + re.sub(r"\D", "", phone[1:])

    return re.sub(r"\D", "", phone)


def make_sms_safe(message):
    """
    Basic GSM text-mode compatibility.
    Removes emoji and unsupported characters from the SOS text.
    """
    return message.encode("ascii", "ignore").decode("ascii")


def read_modem_response(modem, timeout=10):
    end_time = time.time() + timeout
    response = ""

    while time.time() < end_time:
        waiting = modem.in_waiting

        if waiting:
            response += modem.read(waiting).decode(
                "utf-8",
                errors="ignore"
            )

            if "OK" in response or "ERROR" in response:
                break

        time.sleep(0.1)

    return response


def send_command(modem, command, timeout=5):
    modem.reset_input_buffer()
    modem.write(f"{command}\r".encode("utf-8"))
    modem.flush()

    return read_modem_response(modem, timeout)


def send_sms(contact, message):
    if not contact:
        return {
            "status": "FAILED",
            "action": "MESSAGE",
            "message": "No contact available."
        }

    name = contact.get("name", "Unknown")
    phone = clean_phone_number(contact.get("phone", ""))

    if not phone:
        return {
            "status": "FAILED",
            "action": "MESSAGE",
            "contact": name,
            "message": "Contact has no valid phone number."
        }

    if SMS_MODE == "DEMO":
        print()
        print("📨 DEMO SMS")
        print("To:", name)
        print("Number:", phone)
        print(message)

        return {
            "status": "PREPARED",
            "action": "MESSAGE",
            "contact": name,
            "phone": phone,
            "message": "Demo SMS prepared."
        }

    try:
        sms_text = make_sms_safe(message)

        with serial.Serial(
            port=MODEM_PORT,
            baudrate=BAUD_RATE,
            timeout=1
        ) as modem:

            response = send_command(modem, "AT")

            if "OK" not in response:
                raise RuntimeError(
                    "GSM modem did not respond. Check COM port and cable."
                )

            response = send_command(modem, "AT+CMGF=1")

            if "OK" not in response:
                raise RuntimeError(
                    "Could not switch the modem to SMS text mode."
                )

            modem.reset_input_buffer()
            modem.write(
                f'AT+CMGS="{phone}"\r'.encode("utf-8")
            )
            modem.flush()

            prompt = read_modem_response(modem, timeout=8)

            if ">" not in prompt:
                raise RuntimeError(
                    f"Modem did not accept SMS recipient: {prompt}"
                )

            # Ctrl+Z tells the modem to send the SMS.
            modem.write(sms_text.encode("ascii") + b"\x1A")
            modem.flush()

            result = read_modem_response(modem, timeout=25)

            if "+CMGS:" not in result or "OK" not in result:
                raise RuntimeError(
                    f"SMS was not confirmed by modem: {result}"
                )

        print(f"📨 SMS SENT to {name}: {phone}")

        return {
            "status": "SENT",
            "action": "MESSAGE",
            "contact": name,
            "phone": phone,
            "message": "SMS sent successfully."
        }

    except Exception as error:
        print("❌ SMS error:", error)

        return {
            "status": "FAILED",
            "action": "MESSAGE",
            "contact": name,
            "phone": phone,
            "message": str(error)
        }