import data_manager
import flight_search
import notification_manager

sht_data = data_manager.DataManager()
f_search = flight_search.FlightSearch()
msngr = notification_manager.NotificationManager()

sht_list = sht_data.return_dest_dct()
print(sht_list)
if not sht_list[0]["iataCode"]:
    for row in sht_list:
        row["iataCode"] = f_search.get_aita(row["city"])
    sht_data.data = sht_list
    sht_data.update_sht_dest()
for city in sht_list:
    flight_data = f_search.get_flights(city["iataCode"])
    if city["lowestPrice"] < flight_data.price:
        msngr.send_msg(
            flight_data.price,
            flight_data.origin_city,
            flight_data.origin_airport,
            flight_data.destination_city,
            flight_data.destination_airport,
            flight_data.out_date,
            flight_data.return_date
        )
