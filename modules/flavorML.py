import pandas as pd
import numpy as np
import sys
import pickle
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from modules.trainModel import get_model
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=sys.maxsize)

le = preprocessing.LabelEncoder()

data = pd.read_csv('../data/wine_data_flavors_prepared.csv', encoding='utf-8')
data['name'] = le.fit_transform(data['name'])

np.save('../data/flavor_classes.npy', le.classes_)

X = data.drop('name', axis='columns').values
y = data['name']

model, X_train, X_test, y_train, y_test = get_model(X, y)

predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)

# pickle.dump(model, open('../data/wine_flavor_model.sav', 'wb'))
