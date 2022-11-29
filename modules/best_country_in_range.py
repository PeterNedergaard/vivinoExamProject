import pandas as pd
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def get_best_in_range(min_price, max_price):
    wine_data = pd.read_csv('data/wine_data_plus.csv', encoding="utf-8")

    range_data = wine_data.drop(wine_data[(wine_data['price'] < min_price) | (wine_data['price'] > max_price)].index)

    df_avg = pd.DataFrame(range_data.groupby('country', as_index=False)['rating'].mean())

    result = df_avg.sort_values(['rating'], ascending=[False]).head(1)['country'].values[0]

    return result
