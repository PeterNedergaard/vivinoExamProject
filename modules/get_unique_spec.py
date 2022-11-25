import pandas as pd
import csv

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

wine_data = pd.read_csv('../data/wine_data.csv', encoding="utf-8")

unique_countries = wine_data['country'].unique()
unique_regions = wine_data['region'].unique()
unique_wineries = wine_data['winery'].unique()

unique_grapes = set()
grapes_list = wine_data['grapes']

for list_of_grapes in grapes_list:
    list_of_grapes = list_of_grapes.removeprefix('[')
    list_of_grapes = list_of_grapes.removesuffix(']')
    list_of_grapes = list_of_grapes.split(',')

    for grape in list_of_grapes:
        unique_grapes.add(grape)


def concat_specs(country, region, winery):
    return ','.join([country, region, winery])


wine_data['country_region_winery'] = wine_data.apply(
    lambda row: concat_specs(row['country'], row['region'], row['winery']), axis=1)

unique_country_region_winery = wine_data['country_region_winery'].unique()


file = open('../data/country_region_winery.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["country_region_winery"])
for item in unique_country_region_winery:
    writer.writerow([item])
file.close()

file = open('../data/grapes.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["grapes"])
for grape in unique_grapes:
    writer.writerow([grape])
file.close()
