import numpy as np
import pandas as pd
from PIL import Image
from collections import OrderedDict
import matplotlib.pyplot as plt

wine_data = pd.read_csv('../data/wine_data.csv', encoding="utf-8")
rating_dict = {}

for rating in wine_data['rating']:
    rating_dict[rating] = 0

for wine_rating in wine_data['rating']:
    for unique_rating in np.load('../data/classes.npy'):
        if wine_rating == unique_rating:
            rating_dict[wine_rating] += 1

ordered_dict = OrderedDict(sorted(rating_dict.items()))

for key in rating_dict:
    if key < 3:
        ordered_dict.pop(key)

plt.bar(list(ordered_dict.keys()), ordered_dict.values())
plt.xlabel('Rating')
plt.ylabel('Number of ratings')

plt.savefig('../images/all_ratings_plot')

image = Image.open('../images/all_ratings_plot.png')
image.thumbnail((400, 300))
image.save('../images/all_ratings_plot.png')
