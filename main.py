import modules.dataFromSoup as Data
import modules.writeToCSV as Write
import pandas as pd

Write.write_data_to_csv(Data.get_wine_data())
# data = pd.read_csv('wine_data.csv', encoding='cp1250')

# print(data)
