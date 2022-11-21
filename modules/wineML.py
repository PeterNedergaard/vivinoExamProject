import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
lab_enc = preprocessing.LabelEncoder()

data = pd.read_csv('../wine_data.csv', encoding='utf-8')

data_test = data
data_test = pd.get_dummies(data_test, columns=['country', 'region', 'winery'])

data_test['rating'] = lab_enc.fit_transform(data_test['rating'])

unique_grapes = set()

for row in data_test['grapes']:
    row_str = str(row)

    row_str = row_str.removeprefix('[')
    row_str = row_str.removesuffix(']')

    split = row_str.split(',')
    for i in range(len(split)):
        unique_grapes.add(split[i])

onehot_grapes = []

i = 1
for grape in unique_grapes:
    print(str(i) + ': ' + grape + ' of ' + str(len(unique_grapes)))
    grape_list = []

    for index in range(len(data_test)):
        if grape in str(data_test[index:index + 1]['grapes']):
            grape_list.append(1)
        else:
            grape_list.append(0)

    onehot_grapes.append(grape_list)
    i += 1


for index in range(len(onehot_grapes)):
    name = list(unique_grapes)[index]

    data_temp = data_test.copy()

    data_temp[name] = onehot_grapes[index]

    data_test = data_temp

data_test = data_test.drop('grapes', axis='columns')

data_test.to_csv('../wine_data_prepared.csv', encoding='utf-8', index=False)
# data_test = pd.read_csv('../wine_data_prepared.csv', encoding='utf-8')

# model = DecisionTreeClassifier()
#
# X = data_test.drop(['rating'], axis='columns').values
#
# y = data_test['rating'].values
#
# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20)
#
# model.fit(X_train, y_train)

# pickle.dump(model, open('../wine_model.sav', 'wb'))

# model = pickle.load(open('wine_model.sav', 'rb'))

# predictions = model.predict(X_test)
# score = accuracy_score(y_test, predictions)
#
# print(score)
