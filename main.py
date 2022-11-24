import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd
import numpy as np
from modules.predict_wine_data import predict_data
import csv
from modules.python_gui import showgui


pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


wine_data = pd.read_csv('data/wine_data.csv', encoding="utf-8")

unique_countries = wine_data['country'].unique()
unqiue_regions = wine_data['region'].unique()
unique_wineries = wine_data['winery'].unique()
unique_grapes = set()

grapes_list = wine_data['grapes']

for list_of_grapes in grapes_list:
    list_of_grapes = list_of_grapes.removeprefix('[')
    list_of_grapes = list_of_grapes.removesuffix(']')
    list_of_grapes = list_of_grapes.split(',')

    for grape in list_of_grapes:
        unique_grapes.add(grape)

file = open('data/grapes.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
# writer.writerow("grapes")
writer.writerow([unique_grapes])

# data = pd.read_csv('data/wine_data_prepared_new.csv', encoding='utf-8')
# print(data)

# predict_data(country='Argentina',region="Alsace Grand Cru 'Kastelberg'",grapes=['Malvasia', 'Moscatel de Alejandría'],winery='Yann Chave')

# countries = pd.read_csv("data/grapes.csv", encoding="utf-8")
# print(countries[5])
# print(type(countries))

showgui()