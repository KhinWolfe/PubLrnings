import requests
from datetime import datetime as dt

PIXELA_END = "https://pixe.la/v1/users"
# https://pixe.la/@frostyfeet
USER_NAME = "frostyfeet"
TOKEN = "sad15s15s1sd5s"
GRAPH_ID = "graph1"
GRAPH_END = f"{PIXELA_END}/{USER_NAME}/graphs"
today = dt.now()
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
graph_params = {
    "id": GRAPH_ID,
    "name": "Duo Lessons",
    "unit": "ea",
    "type": "int",
    "color": "sora",

}
headers = {
    "X-USER-TOKEN": TOKEN
}
formatted_date = today.strftime("%Y%m%d")
graph_post_params = {
    "date": formatted_date,
    "quantity": "3"
}
GRAPH_POST_END = f"{PIXELA_END}/{USER_NAME}/graphs/{GRAPH_ID}"
GRAPH_PUT_END = f"{PIXELA_END}/{USER_NAME}/graphs/{GRAPH_ID}/{formatted_date}"
graph_put_params = {
    "quantity": "6",
}
graph_del_params = {

}
# response = requests.post(url=PIXELA_END, json=user_params)
# print(response.text)
# response = requests.post(url=GRAPH_END, json=graph_params, headers=headers)
# print(response.text)
# response = requests.post(url=GRAPH_POST_END, json=graph_post_params, headers=headers)
# print(response.text)
# response = requests.put(url=GRAPH_PUT_END, json=graph_put_params, headers=headers)
# print(response.text)
response = requests.delete(url=GRAPH_PUT_END, headers=headers)
print(response.text)
