import requests

POST_END = "https://api.sheety.co/202c0c6a43671773ef2da9d816fa896e/flightDeals/prices"


class DataManager:
    def __init__(self):
        self.response = requests.get(url=POST_END)
        self.data = []

    def return_dest_dct(self):
        response = requests.get(url=POST_END)
        self.data = response.json()["prices"]
        return self.data

    def update_sht_dest(self):
        for city in self.data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{POST_END}/{city['id']}", json=new_data)
            print(response.text)
