import numpy as np
from sklearn import preprocessing
import pandas as pd
import pickle

def predict_data(grapes, winery, country, region):
    le = preprocessing.LabelEncoder()
    le.classes_ = np.load('data/classes.npy')

    empty_predict = pd.read_csv('data/empty_predict.csv')
    # print(empty_predict)

    winery = 'winery_' + winery
    country = 'country_' + country
    region = 'region_' + region

    spec_array = [winery,country,region]

    for grape in grapes:
        spec_array.append(grape)


    for s in spec_array:
        empty_predict[s] = 1

    model = pickle.load(open('data/wine_model.sav', 'rb'))

    # print(empty_predict)

    prediction = model.predict(empty_predict)

    return le.inverse_transform(prediction)[0]





