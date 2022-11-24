import numpy as np


def get_average_deviation(predictions, y_train):

    deviations = []
    for i in range(len(predictions)):
        print('Pred: ' + str(predictions[i]))
        print('Actual: ' + str(y_train[i]))
        print('-------------------------------')

        deviations.append(round(predictions[i] - y_train[i], 2))

    return round(sum(abs(np.array(deviations))) / len(deviations), 2)
