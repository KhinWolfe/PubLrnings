import smtplib
import datetime as dt

def send_mail():
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="17SettingFootsteps^")
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tunneyhansen@gmail.com",
            msg=f"Subject:Week Quote\n\n{qt}".encode("utf8"))

datetime = dt.datetime.now()
