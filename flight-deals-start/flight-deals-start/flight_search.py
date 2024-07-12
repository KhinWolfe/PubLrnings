import requests
import datetime as dt
import flight_data

FLIGHT_SEARCH_LOCATION_END = "https://api.tequila.kiwi.com/locations/query"
FLIGHT_SEARCH_END = "https://api.tequila.kiwi.com/v2/search"
FLY_FROM = "LON"
API_KEY = "Dx120fWyGA2F0v8CafcaJoL8c9SX7jtx"
headers = {
    "apikey": API_KEY,
}


class FlightSearch:
    def __init__(self):
        today = dt.datetime.now()
        self.date_from = (today + dt.timedelta(days=1)).strftime("%d/%m/%Y")
        self.date_to = (today + dt.timedelta(days=6 * 30)).strftime("%d/%m/%Y")

    def get_aita(self, location):
        aita_params = {"term": location}
        response = requests.get(url=FLIGHT_SEARCH_LOCATION_END, params=aita_params, headers=headers)
        return response.json()["locations"][0]["code"]

    def get_flights(self, fly_to):
        params = {
            "fly_from": FLY_FROM,
            "fly_to": fly_to,
            "date_from": self.date_from,  # "dd/mm/yyyy"
            "date_to": self.date_to,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }
        response = requests.get(url=FLIGHT_SEARCH_END, params=params, headers=headers)
        try:
            reply_data = response.json()["data"][0]
        except IndexError:
            print(f"No flights found for {fly_to}.")
            return None

        f_data = flight_data.FlightData(
            price=reply_data["price"],
            origin_city=reply_data["route"][0]["cityFrom"],
            origin_airport=reply_data["route"][0]["flyFrom"],
            destination_city=reply_data["route"][0]["cityTo"],
            destination_airport=reply_data["route"][0]["flyTo"],
            out_date=reply_data["route"][0]["local_departure"].split("T")[0],
            return_date=reply_data["route"][1]["local_departure"].split("T")[0]
        )
        return f_data
