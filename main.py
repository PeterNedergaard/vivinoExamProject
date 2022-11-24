import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd
import numpy as np
from modules.predict_wine_data import predict_data
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

# data = pd.read_csv('data/wine_data_prepared_new.csv', encoding='utf-8')
# print(data)

predict_data(1,1,1,1)
