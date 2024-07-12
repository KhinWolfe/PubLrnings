import os
from pprint import pprint
import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/202c0c6a43671773ef2da9d816fa896e/flightDeals/prices"
SHEETY_USERS_ENDPOINT = "https://api.sheety.co/202c0c6a43671773ef2da9d816fa896e/flightDeals/users"
headers = {
  "Authorization": f"Bearer sdafdsfdsafsdgf",
  "Content-Type": "application/json"
}

class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.email_list = []

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=headers)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=headers
            )
            print(response.text)
    def get_email_list(self):
        response = requests.get(url=SHEETY_USERS_ENDPOINT, headers=headers)
        data = response.json()["users"]
        self.email_list = [row["email"] for row in data]
        return self.email_list