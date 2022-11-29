import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd
import numpy as np
import csv
from modules.python_gui import show_gui

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# wine_data = pd.read_csv('data/wine_data_plus.csv', encoding="utf-8")
# print(wine_data)

# print(pd.read_csv('data/flavors.csv', encoding="utf-8"))
show_gui()
