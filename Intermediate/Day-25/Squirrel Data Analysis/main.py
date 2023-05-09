import pandas as pd


data = pd.read_csv("Data.csv")

squirrel_color = data["Primary Fur Color"]
gray_squirrels = len(data[squirrel_color == "Gray"])
cinnamon_squirrels = len(data[squirrel_color == "Cinnamon"])
black_squirrels = len(data[squirrel_color == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [gray_squirrels, cinnamon_squirrels, black_squirrels]
}

df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_color_count.csv")

