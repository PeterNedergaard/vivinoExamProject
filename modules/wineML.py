import numpy
import pandas as pd
import numpy as np
import sys
import pickle
from sklearn import preprocessing
from sklearn.metrics import accuracy_score
from modules.trainModel import get_model
from calcDeviation import get_average_deviation
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)
np.set_printoptions(threshold=sys.maxsize)

le = preprocessing.LabelEncoder()

data = pd.read_csv('../data/wine_data_prepared_new.csv', encoding='utf-8')
data['rating'] = le.fit_transform(data['rating'])

# numpy.save('../data/classes.npy', le.classes_)

X = data.drop(['rating'], axis='columns').values
y = data['rating'].values

model, X_train, X_test, y_train, y_test = get_model(X, y)

predictions = model.predict(X_test)
score = accuracy_score(y_test, predictions)

print('Score: ' + str(score))
print('Average deviation: ' + str(get_average_deviation(le.inverse_transform(predictions), le.inverse_transform(y_test))))

# pickle.dump(model, open('../data/wine_model.sav', 'wb'))
# model = pickle.load(open('wine_model.sav', 'rb'))
