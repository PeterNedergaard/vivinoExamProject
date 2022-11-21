import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from modules.trainModel import get_model
from calcDeviation import get_average_deviation
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
lab_enc = preprocessing.LabelEncoder()


data = pd.read_csv('../wine_data_preparedTest.csv', encoding='utf-8')

data['rating'] = lab_enc.fit_transform(data['rating'])

X = data.drop(['rating'], axis='columns').values
y = data['rating'].values

X_train, X_test, y_train, y_test, model = get_model(X, y)

model.fit(X_train, y_train)

# pickle.dump(model, open('../wine_model.sav', 'wb'))

# model = pickle.load(open('wine_model.sav', 'rb'))

predictions = model.predict(X_test)

print(get_average_deviation(lab_enc.inverse_transform(predictions), lab_enc.inverse_transform(y_train)))

score = accuracy_score(y_test, predictions)
print(score)
