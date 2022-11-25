import matplotlib.pyplot as plt
import pandas as pd
from collections import OrderedDict

wine_data = pd.read_csv('../data/wine_data.csv', encoding="utf-8")

df_avg = pd.DataFrame(wine_data.groupby('country', as_index=False)['rating'].mean()).head(10)

ordered_df_avg = df_avg.sort_values(['rating'], ascending=[False])

rating_dict = dict(zip(ordered_df_avg['country'], round(ordered_df_avg['rating'], 3)))

plt.figure(figsize=(7, 6))
plt.bar(rating_dict.keys(), rating_dict.values())
plt.xticks(rotation=30, ha='right')
plt.ylabel('Avg. rating')

plt.savefig('../images/top10_plot')
