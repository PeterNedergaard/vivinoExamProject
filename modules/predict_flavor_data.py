import numpy as np
from sklearn import preprocessing
import pandas as pd
import pickle
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)


def predict_flavor_data(flavors):
    print('Predicting flavor...')

    le = preprocessing.LabelEncoder()
    le.classes_ = np.load('data/flavor_classes.npy', allow_pickle=True)

    empty_predict = pd.read_csv('data/empty_flavor_predict.csv')

    spec_array = []

    for flavor in flavors:
        spec_array.append(flavor)

    for s in spec_array:
        empty_predict[s] = 1

    model = pickle.load(open('data/wine_flavor_model.sav', 'rb'))

    prediction = model.predict(empty_predict)

    return le.inverse_transform(prediction)[0]


# print(predict_flavor_data(['chocolate', 'cocoa']))
