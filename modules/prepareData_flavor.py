import pandas as pd
import re
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def clean_flavor_string(flavor_string):
    flavor_string = flavor_string.removeprefix('[')
    flavor_string = flavor_string.removesuffix(']')

    return flavor_string


def check_for_year(wine_name):
    pattern = r'\d{4}'

    return re.sub(pattern, '', wine_name)


def prepare_data():
    data = pd.read_csv('../data/wine_data_flavors.csv', encoding='utf-8')

    data['flavors'] = data['flavors'].apply(clean_flavor_string)

    data = pd.concat([data.drop('flavors', axis='columns'), data['flavors'].str.get_dummies(sep=',')], axis='columns')

    data['name'] = data['name'].apply(check_for_year)

    no_dupes_data = data.drop_duplicates(subset=['name'], keep='first')

    no_dupes_data.to_csv('../data/wine_data_flavors_prepared.csv', encoding='utf-8', index=False)


prepare_data()
