import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

wine_data = pd.read_csv('../data/wine_data_prices.csv', encoding="utf-8")

print(wine_data)
