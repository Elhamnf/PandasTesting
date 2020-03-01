import pandas as pd
import matplotlib

wine_reviews = pd.read_csv('winemag-data-130k-v2.csv', index_col=0)
print(wine_reviews.head())
wine_reviews['points'].plot.hist()
wine_reviews['points'].value_counts().sort_index().plot.bar()
print(wine_reviews['points'].value_counts().sort_index().plot.bar())
import matplotlib.pyplot as plt

# create figure and axis
fig, ax = plt.subplots()
# plot histogram
ax.hist(wine_reviews['points'])
# set title and labels
ax.set_title('Wine Review Scores')
ax.set_xlabel('Points')
ax.set_ylabel('Frequency')
print(fig, ax)


print(wine_reviews['points'].value_counts().sort_index().plot.bar())