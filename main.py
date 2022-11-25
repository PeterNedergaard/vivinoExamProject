import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd
import numpy as np
from modules.predict_wine_data import predict_data
import csv
from modules.python_gui import show_gui

pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# wine_data = pd.read_csv('data/wine_data.csv', encoding="utf-8")

# predict_data(1,1,1,1)

print(pd.read_csv('data/empty_predict.csv', encoding='utf-8'))

show_gui()
