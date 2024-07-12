from twilio.rest import Client
import os
import smtplib

TWILIO_SID = os.environ["TWIL_SID"]
TWILIO_AUTH_TOKEN = os.environ["TWIL_AUTH"]
TWILIO_VIRTUAL_NUMBER = os.environ["TWIL_VIR_NUM"]
TWILIO_VERIFIED_NUMBER = os.environ["TWIL_VER_NUM"]
MY_EMAIL = "blank"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)

    def send_email(self, address, msg):
        with smtplib.SMTP("outlook.office365.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=pass)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=address,
                msg=f"Subject:Great Deal!\n\n{msg}".encode("utf8")
            )
