import pandas as pd
import csv
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

wine_data = pd.read_csv('../data/wine_data.csv', encoding="utf-8")


unique_countries = wine_data['country'].unique()
unique_regions = wine_data['region'].unique()
unique_wineries = wine_data['winery'].unique()

print(unique_wineries)

unique_grapes = set()

grapes_list = wine_data['grapes']

for list_of_grapes in grapes_list:
    list_of_grapes = list_of_grapes.removeprefix('[')
    list_of_grapes = list_of_grapes.removesuffix(']')
    list_of_grapes = list_of_grapes.split(',')

    for grape in list_of_grapes:
        unique_grapes.add(grape)

file = open('../data/grapes.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(["grapes"])
for grape in unique_grapes:
    writer.writerow([grape])
file.close()

# file = open('../data/wineries.csv', 'w', encoding='utf-8')
# writer = csv.writer(file)
# writer.writerow(["wineries"])
# for winery in unique_wineries:
#     writer.writerow([winery])
# file.close()
#
# file = open('../data/countries.csv', 'w', encoding='utf-8')
# writer = csv.writer(file)
# writer.writerow(["countries"])
# for country in unique_countries:
#     writer.writerow([country])
# file.close()
#
# file = open('../data/regions.csv', 'w', encoding='utf-8')
# writer = csv.writer(file)
# writer.writerow(["regions"])
# for region in unique_regions:
#     writer.writerow([region])
# file.close()

for row in wine_data:


# file = open('../data/regions.csv', 'w', encoding='utf-8')
# writer = csv.writer(file)
# writer.writerow(["regions"])
# for region in unique_regions:
#     writer.writerow([region])
# file.close()
