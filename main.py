import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd

data = pd.read_csv('wine_data.csv', encoding='utf-8')

print(data)
