import pandas as pd

def prepare_data():
    data = pd.read_csv('../wine_data.csv', encoding='utf-8')

    data_test = data
    data_test = pd.get_dummies(data_test, columns=['country', 'region', 'winery'])

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


prepare_data()
