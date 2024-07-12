# # with open("weather_data.csv") as file:
# #     list = file.readlines()
# #
# # print(list)
#
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("weather_data.csv")
# # print(data["temp"])
# #
# # temp_list = data["temp"].to_list()
# # average = sum(temp_list) / len(temp_list)
# # print(data["temp"].mean())
# #
# # print(average)
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.temp * 9 / 5 + 32)

data = pandas.read_csv("sqrl_data.csv")
sqrl_color = data["Primary Fur Color"].tolist()

print(sqrl_color)
gray_count = len(data[data["Primary Fur Color"] == "Gray"])
cinnamon_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_count = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur ColoR": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_count, cinnamon_count, black_count]
}
df = pandas.DataFrame(data_dict)
df.to_csv("sqrl_cnt.csv")