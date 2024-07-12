from twilio.rest import Client

account_sid = ""
auth_token = ""
twilio_code = ""
twilio_num = ""


class NotificationManager:
    # This class is responsible for sending notifications with the deal flight details.
    pass

    def send_msg(self, price, f_city, f_aita, t_city, t_aita, f_date, r_date):
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"Low price alert! only ${price} to fly from {f_city}-{f_aita} to "
                 f"{t_city}-{t_aita}, from {f_date} to {r_date}.",
            from_="",
            to=""
        )
        print(message.sid)
