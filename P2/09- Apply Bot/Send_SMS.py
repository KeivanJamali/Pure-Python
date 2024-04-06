from twilio.rest import Client

# Your Twilio account credentials
account_sid = ""
auth_token = ""

# Create a Twilio client
client = Client(account_sid, auth_token)


# Function to send SMS
def send_sms(message_):
    try:
        mg = client.messages.create(
            body=message_,
            from_='+12058464951',
            to='+989101511983'
        )
        print("SMS sent successfully!")
    except Exception as e:
        print(f"Error sending SMS: {e}")

