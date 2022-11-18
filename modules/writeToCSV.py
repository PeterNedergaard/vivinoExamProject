import csv


def write_data_to_csv(data):
    file = open('./wine_data.csv', 'w', encoding='utf-8')
    writer = csv.writer(file)

    writer.writerow(['grape', 'region', 'country', 'winery', 'rating'])
    for wine in data:
        writer.writerow(wine.values())

    file.close()
