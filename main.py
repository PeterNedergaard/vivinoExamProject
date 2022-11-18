import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd
# pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv('wine_data.csv', encoding='utf-8')
print(data)
