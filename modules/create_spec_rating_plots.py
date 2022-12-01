import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats


def create_plots(spec_name):
    plt.clf()

    wine_data = pd.read_csv('../data/wine_data.csv', encoding="utf-8")

    if spec_name != 'country':

        csv_name = ''
        if spec_name == 'region':
            csv_name = 'regions'
        elif spec_name == 'winery':
            csv_name = 'wineries'
        else:
            csv_name = spec_name

        spec_dict = {}
        for spec in pd.read_csv('../data/' + csv_name + '.csv', encoding="utf-8")[csv_name].values:
            spec_dict[spec] = len(wine_data[wine_data[spec_name] == spec])

        q = np.quantile(list(spec_dict.values()), 0.92)

        outlier_list = []
        for key, value in spec_dict.items():
            if value < q:
                outlier_list.append(key)

        wine_data = wine_data[~wine_data[spec_name].isin(outlier_list)]


    df_country_avg = pd.DataFrame(wine_data.groupby(spec_name, as_index=False)['rating'].mean())

    ordered_country_avg = df_country_avg.sort_values(['rating'], ascending=[False])

    ordered_country_avg = ordered_country_avg.reset_index(drop=True)

    x_list = [x + 1 for x in ordered_country_avg.index.values.tolist()]

    rating_dict = dict(zip(ordered_country_avg[spec_name], round(ordered_country_avg['rating'], 3)))

    # plt.figure(figsize=(7, 6))
    plt.bar(rating_dict.keys(), rating_dict.values())
    plt.title('Correlation between ' + spec_name + ' and avg. rating')
    plt.xticks([])
    plt.ylabel('Avg. rating')

    slope, intercept, r, p, std_err = stats.linregress(x_list, ordered_country_avg['rating'])

    def myfunc(x):
        return slope * x + intercept

    y_list = list(map(myfunc, x_list))

    plt.plot(x_list, y_list, color='red')

    print('a = ' + str(slope))

    plt.xlabel('Slope = ' + str(round(slope, 6)))

    plt.savefig('../images/correlation_plot_' + spec_name)


create_plots('country')
create_plots('region')
create_plots('winery')
create_plots('grapes')
