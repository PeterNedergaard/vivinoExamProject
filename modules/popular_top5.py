import pandas as pd
import re
import matplotlib.pyplot as plt
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

countries = pd.read_csv('../data/countries.csv', encoding="utf-8")


def check_for_year(wine_name):
    pattern = r'\d{4}'

    return re.sub(pattern, '', wine_name)


def get_popular_top5(country):
    wine_data = pd.read_csv('../data/wine_data_plus.csv', encoding="utf-8")

    country_data = wine_data[(wine_data['country'] == country)]

    sorted_country_data = country_data.sort_values(['ratings_count'], ascending=[False])

    sorted_country_data['name'] = sorted_country_data['name'].apply(check_for_year)

    no_dupes_data = sorted_country_data.drop_duplicates(subset=['name'], keep='first').head(5)

    popular_dict = dict(zip(no_dupes_data['name'], round(no_dupes_data['ratings_count'], 3)))

    plt.figure(figsize=(7, 6))
    plt.bar(popular_dict.keys(), popular_dict.values(), width=0.2)
    plt.xticks(rotation=-15, ha='left')
    plt.ylabel('Rating count')
    plt.tight_layout()

    plt.savefig('../images/popular_top5_plots/top5_' + country)


for each in countries['countries']:
    get_popular_top5(each)
