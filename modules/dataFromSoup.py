import modules.webScraper as Scrape


def get_wine_data():
    result_div = Scrape.get_wine_soup().findAll('div', {'class': 'explorerPage__results--3wqLw'})[0]

    wine_data = []
    for ele in result_div.findNext('div'):
        if str(ele) == '<span data-testid="sentinel"></span>':
            continue

        grape_div = ele.findNext('div', {'class': 'wineInfoVintage__vintage--VvWlU wineInfoVintage__truncate--3QAtw'})
        region_country_div = ele.findNext('div', {'class': 'wineInfoLocation__regionAndCountry--1nEJz'})
        winery_div = ele.findNext('div', {'class': 'wineInfoVintage__truncate--3QAtw'})
        rating_div = ele.findNext('div', {'class': 'vivinoRating_averageValue__uDdPM'})

        # grape = ''
        # if grape_div.text.endswith('N.V.'):
        #     grape = 'Blend'

        split_country_region = region_country_div.text.split(', ')

        wine_dict = {
            'grape': grape_div.text,
            'region': split_country_region[0],
            'country': split_country_region[1],
            'winery': winery_div.text,
            'rating': rating_div.text
        }

        wine_data.append(wine_dict)

    print(len(wine_data))

    return wine_data
