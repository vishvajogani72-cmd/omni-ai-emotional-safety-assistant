import sos_message

message = sos_message.generate_sos_message(
    emergency_type="FOLLOWING",
    risk_level="CRITICAL",
    risk_score=100,
    risk_reason="Someone may be following the user"
)

message = sos_message.generate_sos_message()

print()
print("================================")
print("         SOS MESSAGE              ")
print("================================")
print(message)
print("================================")