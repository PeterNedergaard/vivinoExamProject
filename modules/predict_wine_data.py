import numpy as np
from sklearn import preprocessing


def predict_data(grapes, winery, country, region):
    le = preprocessing.LabelEncoder()
    le.classes_ = np.load('data/classes.npy')

