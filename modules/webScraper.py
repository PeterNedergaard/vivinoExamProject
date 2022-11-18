import bs4
import time
import keyboard
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.chrome import ChromeDriverManager


def get_wine_soup():
    url = 'https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1MjUwUEuutHXxVksGEt5qBUDp9DTbssSizNSSxBy1_KIU25TU4mS1_KRK26LEksy89OL45PzSvBIAZGAZAw%3D%3D'

    options = Options()
    options.headless = True

    firefox_profile = webdriver.FirefoxProfile()
    firefox_profile.set_preference('permissions.default.image', 2)
    firefox_profile.set_preference('dom.ipc.plugins.enabled.libflashplayer.so', 'false')

    # browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    browser = webdriver.Firefox(options=options, firefox_profile=firefox_profile)

    print('Opening webpage...')
    browser.get(url)

    print('Webpage loading...')
    time.sleep(5)

    # a = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div')))
    # a = browser.find_elements(By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div')

    max_scroll_tries = 50
    scroll_tries = 0
    scroll_num = 0

    wine_amount_target = 200
    wine_amount = 0
    i = 1

    # Start scroll loop
    while True:
        current_height = browser.execute_script("return document.body.scrollHeight")

        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(0.5)

        # print('mod:' + str(i % 20))
        # if i % 100 == 0:
        #     time.sleep(2)
        #     current_amount = get_wine_amount(bs4.BeautifulSoup(browser.page_source, 'lxml'))
        #     print('Current wine amount: ' + str(current_amount) + ' of 30.000')
        #
        #     if current_amount == wine_amount:
        #         break
        #
        #     wine_amount = current_amount
        #
        # i += 1

        new_height = browser.execute_script("return document.body.scrollHeight")

        if new_height > current_height+100:
            print('NewHeight: ' + str(new_height))
            print('CurrentHeight: ' + str(current_height))

            scroll_num += 1
            scroll_tries = 0
            print('Scroll: ' + str(scroll_num) + ' out of 1205')

        if new_height == current_height:
            scroll_tries += 1
            print('Tried scrolling: ' + str(scroll_tries))

        if scroll_num >= 1205:
            print('Done scrolling')
            break

        if scroll_tries >= max_scroll_tries:
            print('Max scroll tries reached')
            break

        if keyboard.is_pressed('q'):
            print('PRESSED Q')
            break

    # End scroll loop

    print('Scraping...')
    soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
    browser.close()

    return soup


def get_wine_amount(soup):
    result_div = soup.findAll('div', {'class': 'explorerPage__results--3wqLw'})[0]

    amount = 0
    for ele in result_div.findNext('div'):
        if str(ele) == '<span data-testid="sentinel"></span>':
            continue
        amount += 1

    return amount
