import sms_gateway


test_contact = {
    "name": "My Test Number",
    "phone": "9999999999"
}

test_message= (
    "OMNIAI TEST MESSAGE\n"
    "This is a safe SMS test. No emergency."
)
result = sms_gateway.send_sms(
    test_contact,
    test_message
)

print()
print("SMS test result:", result)