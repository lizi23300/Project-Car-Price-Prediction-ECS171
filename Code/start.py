import pandas as pd

pandaDataFrame = pd.read_csv("used_cars.csv")

X = pandaDataFrame.drop(columns="price")
y = pandaDataFrame["price"]