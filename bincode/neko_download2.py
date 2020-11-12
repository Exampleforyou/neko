import os

import requests
import re
from bs4 import BeautifulSoup as bs4
from selenium import webdriver
import time

URL = 'https://www.pinterest.ru/mihailr5x/neko-tyan/'


def get_html(page):
    with open(file='neko.html', mode='w', encoding='utf-8') as file:
        file.write(page)

i = 0
def get_all_html():
    global driver
    global scrolls
    global SCROLL_PAUSE_TIME
    print('''
        Насколько много надо неко?
        ВАМ НУЖНО 1000 НЕКО))))
        Если что сейчас откроется браузер и всё сделает сам
    ''')
    scrolls = int(input('Говори сколько СТРАНИЦ с неко надо подгрузить? 1 страница - 35 неко примерно: '))
    SCROLL_PAUSE_TIME = int(input('''Насколько у тебя плохой комп? ( время перерыва подгрузки страниц
                 если сделать мало то скрипт не сработает нужное кол-во раз
                 20 - полная хуйня
                 10 - полная хуйня
                 5 -  ноут
                 1-2  Стационарный пк( норм комп )
                 '''))
    int(input())
    driver = webdriver.Chrome()
    driver.get(URL)

    while i < scrolls:
        scrolling(scrolls)

    return driver.page_source


def scrolling(scrolls):
    global i
    # Get scroll height
    last_height = driver.execute_script("return document.body.scrollHeight")

    while i < scrolls:
        i += 1
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)

        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
        print(i, ' страница пошла')
    return i


def code():
    with open(file='neko.html', mode='r', encoding='utf-8') as file:
        html = file.read()
    parser = bs4(html, 'html.parser')
    results = parser.find_all('img')
    if len(results) > 100:
        print('Результаты найдены')
    else:
        print('длина кода итогового -', len(results))
    count = 0
    for result in results:
        count += 1
        nekoSrc = result['src']
        print(count, 'неко в базе')
        neko = requests.get(nekoSrc)
        with open(f'nekobase/neko{count}.jpg', mode='wb', ) as nekoFile:
            nekoFile.write(neko.content)



get_html(get_all_html())
code()

num_files = sum(os.path.isfile(os.path.join('nekobase/', f)) for f in os.listdir('nekobase/'))
print(num_files)
input()