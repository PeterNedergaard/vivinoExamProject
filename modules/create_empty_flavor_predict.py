import pandas as pd


data = pd.read_csv('../data/wine_data_flavors_prepared.csv', encoding='utf-8', nrows=1)

data_empty = data.drop('name', axis='columns')

for col in data_empty.columns:
    data_empty[col] = 0

data_empty.to_csv('../data/empty_flavor_predict.csv', encoding='utf-8', index=False)
