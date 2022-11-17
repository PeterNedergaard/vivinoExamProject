import bs4
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options


def get_wine_soup():
    url = 'https://www.vivino.com/explore?e=eJzLLbI1VMvNzLM1UMtNrLA1MjUwUEuutHXxVksGEt5qBUDp9DTbssSizNSSxBy1_KIU25TU4mS1_KRK26LEksy89OL45PzSvBIAZGAZAw%3D%3D'

    options = Options()
    options.headless = True

    # browser = webdriver.Firefox(service=Service(GeckoDriverManager().install()), options=options)
    browser = webdriver.Firefox(options=options)

    print('Opening webpage...')
    browser.get(url)

    print('Webpage loading...')
    time.sleep(5)

    # a = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div')))
    # a = browser.find_elements(By.XPATH, '/html/body/div[2]/div[4]/div/div/div[2]/div[2]/div[1]/div[1]/div')

    print('Scraping...')
    soup = bs4.BeautifulSoup(browser.page_source, 'lxml')
    browser.close()

    return soup
