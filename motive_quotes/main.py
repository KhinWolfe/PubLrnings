import smtplib

my_email = "plrning@outlook.com"
def send_mail(qt):
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="17SettingFootsteps^")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tunneyhansen@gmail.com",
            msg=f"Subject:Week Quote\n\n{qt}".encode("utf8"))

import datetime as dt
import random
now = dt.datetime.now()
weekday = now.weekday()
print(weekday)
if weekday == 5:
    with open("quotes.txt", "r", encoding="utf8") as file:
        list_quotes = file.readlines()
        rand_qt = random.choice(list_quotes)
        send_mail(rand_qt)