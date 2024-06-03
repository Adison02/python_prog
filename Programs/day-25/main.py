# with open("weather_data.csv", mode="r") as file:
#     data = file.readlines()
# # print(data)
#
# # import csv
# #
# # with open("weather_data.csv") as csv_file:
# #     csv_reader = csv.reader(csv_file)
# #     temperatures = []
# #     for row in csv_reader:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)

# with open("index.html", mode="w") as file:
#     file.write(data.to_html())

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(data["temp"].mean())
# print(data["temp"].max())

# import pandas
# data = pandas.read_csv("weather_data.csv")

# Get data in columns
# print(data["day"])
# print(data.day)

# Get data in Row
# print(data[data["day"] == "Monday"])
# print(data[data["temp"] == data["temp"].max()])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday["temp"])
# print(monday_temp, "In celsius")
# print(monday_temp*1.8+32, "In fahrenheit")

# Create a data frame from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

squirrel_count_dict = {
    "Fur Color": [],
    "Count": []
}

import pandas
squirrel_csv = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

for animal_color in squirrel_csv["Primary Fur Color"].unique():
    if not pandas.isna(animal_color):

        animal_count = len(squirrel_csv[squirrel_csv["Primary Fur Color"] == animal_color])
        squirrel_count_dict["Fur Color"].append(animal_color)
        squirrel_count_dict["Count"].append(animal_count)

data = pandas.DataFrame(squirrel_count_dict)
data.to_csv("data.csv")







