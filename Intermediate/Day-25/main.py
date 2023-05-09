# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#     print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(type(data))  # DataFrame is 2 dimensional data (aka. Table)
# print(type(data["temp"]))  # Series is 1 dimensional data ( Single row-column )

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# monday_temp = monday.temp
#
# monday_f_temp = monday_temp*(9/5) + 32
# print(monday_f_temp)

# Create a DataFrame from scratch
data_dict = {
    "student": ["amy", "moe", "max"],
    "scores": [10, 9, 10]
}
data = pandas.DataFrame(data_dict)
# print(data)
data.to_csv("scores.csv")