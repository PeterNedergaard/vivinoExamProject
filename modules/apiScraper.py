import requests
import csv
import math
import threading

# file = open('../data/wine_data_plusTEST.csv', 'w', encoding='utf-8')
# writer = csv.writer(file)
# writer.writerow(['grapes', 'region', 'country', 'winery', 'rating', 'price', 'ratings_count', 'name', 'flavors'])

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


# while current_max_price <= max_price:
#     params['price_range_max'] = current_max_price
#     params['price_range_min'] = current_min_price
#
#     print('Price range: ' + str(params['price_range_min']) + '-' + str(params['price_range_max']))
#
#     r = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
#     wine_amount = r.json()['explore_vintage']['records_matched']
#
#     page_amount = math.ceil(wine_amount / 25)
#
#     if wine_amount <= 25:
#         page_amount = 1
#
#     print('pages: ' + str(page_amount))
#     print('------------------')
#
#     for i in range(page_amount):
#         params['page'] = i + 1
#         print('Page: ' + str(params['page']))
#
#         r = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
#         matches = r.json()['explore_vintage']['matches']
#
#         for match in matches:
#             if str(match['vintage']['wine']['style']) == 'None' \
#                     or str(match['vintage']['wine']['region']) == 'None' \
#                     or str(match['vintage']['wine']['winery']) == 'None' \
#                     or str(match['vintage']['wine']['statistics']) == 'None'\
#                     or str(match['vintage']['wine']['taste']['flavor']) == 'None':
#                 continue
#
#             region = match['vintage']['wine']['region']['name']
#             country = match['vintage']['wine']['region']['country']['name']
#             winery = match['vintage']['wine']['winery']['name']
#             rating = match['vintage']['wine']['statistics']['ratings_average']
#             price = match['price']['amount']
#             ratings_amount = match['vintage']['statistics']['wine_ratings_count']
#             name = match['vintage']['name']
#             print(name)
#
#             grapes = []
#             for grape in match['vintage']['wine']['style']['grapes']:
#                 grapes.append(grape['name'])
#
#             flavors = []
#             for flavor in match['vintage']['wine']['taste']['flavor']:
#                 for key in flavor:
#                     index = 0
#                     if str(key).endswith('keywords'):
#                         for keyword in dict(flavor)[key]:
#                             if index >= 3:
#                                 break
#
#                             flavors.append(keyword['name'])
#                             index += 1
#
#             writer.writerow(['[' + ','.join(grapes) + ']', region, country, winery, rating, price, ratings_amount, name, '[' + ','.join(flavors) + ']'])
#
#     current_max_price += 15
#     current_min_price = current_max_price - 14
#
#     if current_max_price == 2505:
#         current_max_price = 2500
#         current_min_price = 2491
#
# file.close()


file = open('../data/wine_data_flavors.csv', 'w', encoding='utf-8')
writer = csv.writer(file)
writer.writerow(['name', 'flavors'])


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
            if str(match['vintage']['wine']['taste']['flavor']) == 'None':
                continue

            name = match['vintage']['name']

            flavors = []
            for flavor in match['vintage']['wine']['taste']['flavor']:
                for key in flavor:
                    index = 0
                    if str(key).endswith('keywords'):
                        for keyword in dict(flavor)[key]:
                            if index >= 3:
                                break

                            flavors.append(keyword['name'])
                            index += 1

            if len(flavors) > 0:
                writer.writerow([name, '[' + ','.join(flavors) + ']'])

    current_max_price += 15
    current_min_price = current_max_price - 14

    if current_max_price == 2505:
        current_max_price = 2500
        current_min_price = 2491

file.close()







# def get_page(range_max, range_min, page_num):
#     my_headers = {
#         'User-Agent': ''
#     }
#
#
#     my_params = {
#         'min_rating': 1,
#         'order_by': 'ratings_count',
#         'order': 'desc',
#         'price_range_max': range_max,
#         'price_range_min': range_min,
#         'page': page_num
#     }
#
#     print('page: ' + str(page_num))
#
#     r = requests.get('https://www.vivino.com/api/explore/explore?', params=my_params, headers=my_headers)
#     matches = r.json()['explore_vintage']['matches']
#
#     for match in matches:
#         if str(match['vintage']['wine']['taste']['flavor']) == 'None':
#             continue
#
#         name = match['vintage']['name']
#
#         flavors = []
#         for flavor in match['vintage']['wine']['taste']['flavor']:
#             for key in flavor:
#                 index = 0
#                 if str(key).endswith('keywords'):
#                     for keyword in dict(flavor)[key]:
#                         if index >= 3:
#                             break
#
#                         flavors.append(keyword['name'])
#                         index += 1
#
#         if len(flavors) > 0:
#             data_list.append([name, '[' + ','.join(flavors) + ']'])
#
#
# threads = []
# data_list = []
#
# while current_max_price <= max_price:
#
#     headers = {
#         'User-Agent': ''
#     }
#
#     params = {
#         'min_rating': 1,
#         'order_by': 'ratings_count',
#         'order': 'desc',
#         'price_range_max': 0,
#         'price_range_min': 0,
#     }
#
#     params['price_range_max'] = current_max_price
#     params['price_range_min'] = current_min_price
#
#     print('Price range: ' + str(params['price_range_min']) + '-' + str(params['price_range_max']))
#     print('------------------')
#
#     re = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
#     wine_amount = re.json()['explore_vintage']['records_matched']
#
#     page_amount = math.ceil(wine_amount / 25)
#
#     if wine_amount <= 25:
#         page_amount = 1
#
#     # print('pages: ' + str(page_amount))
#
#     for i in range(page_amount):
#         threads.append(threading.Thread(target=get_page, args=(current_max_price, current_min_price, i + 1,)))
#
#     current_max_price += 15
#     current_min_price = current_max_price - 14
#
#     if current_max_price == 2505:
#         current_max_price = 2500
#         current_min_price = 2491
#
# print('Starting threads...')
# for thread in threads:
#     thread.start()
#
# print('Waiting for threads to finish...')
# for thread in threads:
#     thread.join()
#
# print('Writing ' + str(len(data_list)) + ' rows to CSV')
# file = open('../data/wine_data_flavors.csv', 'w', encoding='utf-8')
# writer = csv.writer(file)
# writer.writerow(['name', 'flavors'])
#
# for wine in data_list:
#     writer.writerow([wine[0], wine[1]])
#
# file.close()











# for i in range(1):
#     params['page'] = i + 1
#     print('Page: ' + str(params['page']))
#
#     r = requests.get('https://www.vivino.com/api/explore/explore?', params=params, headers=headers)
#     matches = r.json()['explore_vintage']['matches']
#
#     wine_amount = r.json()['explore_vintage']['records_matched']
#     page_amount = math.ceil(wine_amount / 25)
#     print('wine amnt:' + str(wine_amount))
#     print('page amnt:' + str(page_amount))
#
#     print(dict(matches[0]['vintage']['wine']['taste'])['flavor'])
#
#     for match in matches:
#         print('-----------------------------------------------')
#         flavors = []
#
#         for flavor in match['vintage']['wine']['taste']['flavor']:
#             for key in flavor:
#                 index = 0
#                 if str(key).endswith('keywords'):
#                     for keyword in dict(flavor)[key]:
#                         if index >= 3:
#                             break
#
#                         flavors.append(keyword['name'])
#                         index += 1
#
#         print(flavors)
#
#     for match in matches:
#         if str(match['vintage']['wine']['style']) == 'None' \
#                 or str(match['vintage']['wine']['region']) == 'None' \
#                 or str(match['vintage']['wine']['winery']) == 'None' \
#                 or str(match['vintage']['wine']['statistics']) == 'None':
#             continue
#
#         region = match['vintage']['wine']['region']['name']
#         country = match['vintage']['wine']['region']['country']['name']
#         winery = match['vintage']['wine']['winery']['name']
#         rating = match['vintage']['wine']['statistics']['ratings_average']
#         price = match['price']['amount']
#         name = match['vintage']['name']
#
#         grapes = []
#         for grape in match['vintage']['wine']['style']['grapes']:
#             grapes.append(grape['name'])
#
#         flavors = []
#         for flavor in match['vintage']['wine']['taste']['flavor']:
#             for key in flavor:
#                 index = 0
#                 if str(key).endswith('keywords'):
#                     for keyword in dict(flavor)[key]:
#                         if index >= 3:
#                             break
#
#                         flavors.append(keyword['name'])
#                         index += 1
