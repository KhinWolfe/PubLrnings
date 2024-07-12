import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

PRICE_ALARM = 200
URL = "https://www.amazon.com/dp/B01NBKTPTS?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"


headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
    "sec-ch-ua": '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "Windows"
}
response = requests.get(url=URL, headers=headers)

soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.find(class_="a-offscreen").getText().split("$")[1])
#price_cents = soup.find(name="span", class_="a-price-fraction").getText()
# combined = float(f"{price}.{price_cents}")
# print(combined)
print(price)

if price < PRICE_ALARM:
    print("ok")
    with smtplib.SMTP("outlook.office365.com") as connection:
        connection.starttls()
        connection.login(user="plrning@outlook.com", password="17SettingFootsteps^")
        connection.sendmail(
            from_addr="plrning@outlook.com",
            to_addrs="wolfekhin@gmail.com",
            msg=f"Subject:Price Alert!\n\nThe current price is ${price}\n\n{URL}.".encode("utf8")
        )

