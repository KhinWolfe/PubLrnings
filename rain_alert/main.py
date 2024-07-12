api_key = ""
MY_LAT = 44.7476
MY_LONG = -87.6225
import requests
from twilio.rest import Client
end_point = "https://api.openweathermap.org/data/2.5/forecast"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "cnt": 4,
}
account_sid = ""
auth_token = ""
twilio_code = ""
twilio_num = ""
response = requests.get(url=end_point, params=parameters)
response.raise_for_status()
data = response.json()


will_rain = False
for item in data["list"]:
    condition_code = (item["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_="",
        to=""
    )
    print(message.status)



