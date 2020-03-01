import pandas as pd
from pandas import DataFrame

reviews = pd.read_csv("ign.csv")
print (reviews.head())

print(reviews.shape)
