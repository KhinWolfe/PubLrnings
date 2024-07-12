##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import smtplib
import datetime as dt
import pandas
import random
letters = ["./letter_templates/letter_1.txt","./letter_templates/letter_2.txt", "./letter_templates/letter_3.txt" ]

def prepare_letter(bday_name):
    r_letter = random.choice(letters)
    with open(r_letter) as letter:
        new_letter = letter.read()
        new_letter = new_letter.replace("[NAME]", bday_name)
        return new_letter

def send_letter(letter, email):
    my_email = "plrning@outlook.com"
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password="17SettingFootsteps^")
        connection.sendmail(
            from_addr=my_email,
            to_addrs=email,
            msg=f"Subject:Happy Birthday!\n\n{letter}".encode("utf8"))

data = pandas.read_csv("birthdays.csv")
bdays = data.to_dict(orient="records")
print(bdays)
today = dt.datetime.now()
print(today.day)
for item in bdays:
    if item["day"] == today.day and item["month"] == today.month:
        letter = prepare_letter(item["name"])
        send_letter(letter, item["email"])