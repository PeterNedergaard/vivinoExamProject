import requests
import csv
import math

file = open('./wine_data2.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['grapes', 'region', 'country', 'winery', 'rating'])

headers = {
    'User-Agent': ''
}

params = {
    'min_rating': 1,
    'order_by': 'ratings_count',
    'order': 'desc',
    'price_range_max': 0,
    'price_range_min': 0,
}

max_price = 2500
current_max_price = 15
current_min_price = 0

while current_max_price <= max_price:
    params['price_range_max'] = current_max_price
    params['price_range_min'] = current_min_price

    print('Price range: ' + str(params['price_range_min']) + '-' + str(params['price_range_max']))

    r = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
    wine_amount = r.json()['explore_vintage']['records_matched']

    page_amount = math.ceil(wine_amount / 25)

    if wine_amount <= 25:
        page_amount = 1

    print('pages: ' + str(page_amount))
    print('------------------')

    for i in range(page_amount):
        params['page'] = i + 1
        print('Page: ' + str(params['page']))

        r = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
        matches = r.json()['explore_vintage']['matches']

        for match in matches:
            if str(match['vintage']['wine']['style']) == 'None' \
                    or str(match['vintage']['wine']['region']) == 'None' \
                    or str(match['vintage']['wine']['winery']) == 'None' \
                    or str(match['vintage']['wine']['statistics']) == 'None':
                continue

            region = match['vintage']['wine']['region']['name']
            country = match['vintage']['wine']['region']['country']['name']
            winery = match['vintage']['wine']['winery']['name']
            rating = match['vintage']['wine']['statistics']['ratings_average']
            grapes = []
            for grape in match['vintage']['wine']['style']['grapes']:
                grapes.append(grape['name'])

            writer.writerow(['[' + ','.join(grapes) + ']', region, country, winery, rating])

    current_max_price += 15
    current_min_price = current_max_price - 14

    if current_max_price == 2505:
        current_max_price = 2500
        current_min_price = 2491

file.close()










# for i in range(1):
#     params['page'] = i+1
#     print('Page: ' + str(params['page']))
#
#     r = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
#     matches = r.json()['explore_vintage']['matches']
#
#     for match in matches:
#         if str(match['vintage']['wine']['style']) == 'None' \
#                 or str(match['vintage']['wine']['region']) == 'None'\
#                 or str(match['vintage']['wine']['winery']) == 'None'\
#                 or str(match['vintage']['wine']['statistics']) == 'None':
#             continue
#
#         region = match['vintage']['wine']['region']['name']
#         country = match['vintage']['wine']['region']['country']['name']
#         winery = match['vintage']['wine']['winery']['name']
#         rating = match['vintage']['wine']['statistics']['ratings_average']
#         grapes = []
#         for grape in match['vintage']['wine']['style']['grapes']:
#             grapes.append(grape['name'])
#
#         writer.writerow(['[' + ','.join(grapes) + ']', region, country, winery, rating])