import pandas as pd
import csv

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

wine_data = pd.read_csv('../data/wine_data_flavors.csv', encoding="utf-8")

unique_flavors = set()

for list_of_flavors in wine_data['flavors']:
    list_str = str(list_of_flavors)

    list_str = list_str.removeprefix('[')
    list_str = list_str.removesuffix(']')

    flavor_split = list_str.split(',')

    for flavor in flavor_split:
        unique_flavors.add(flavor)


file = open('../data/flavors.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['flavors'])
for item in unique_flavors:
    writer.writerow([item])
file.close()
