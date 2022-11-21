import numpy as np


def get_average_deviation(predictions, y_train):

    deviations = []
    for i in range(len(predictions)):
        deviations.append(round(predictions[i] - y_train[i], 2))

    return round(sum(abs(np.array(deviations))) / len(deviations), 2)
