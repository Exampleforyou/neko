import time
import json

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup as bs


class NekoBot:
    NekoURL = "https://www.instagram.com/"
    login = "ksiolove"
    password = "vadim2001"

    driver = ''

    def __init__(self, login, password):
        self.login = login
        self.password = password

        driver = webdriver.Chrome()
        driver.get(self.NekoURL)
        self.driver = driver
        time.sleep(3)
        neko = driver.find_element_by_css_selector('img.hCL kVc L4E MIw')

        try:
            notNow = driver.find_element_by_css_selector("button.aOOlW.HoLwm")
        except:
            time.sleep(1)
            driver.get(self.instagramURL)
            notNow = driver.find_element_by_css_selector("button.aOOlW.HoLwm")
        notNow.click()

        driver.get(self.main_page)

    def GetFollowersCode(self):
        driver = self.driver

        followers_count = driver.find_element_by_css_selector('ul:nth-child(2) li a span')
        print(followers_count.text)

        followers_link = driver.find_element_by_css_selector('ul:nth-child(2) li a')
        followers_link.click()
        # Go to followers list

        time.sleep(1)

        follower = driver.find_element_by_css_selector('div li:nth-child(1) a.FPmhX.notranslate._0imsa ')
        print(follower.text)

        followers_section = driver.find_element_by_css_selector('div.isgrP')

        driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", followers_section)

        return driver.page_source

    @staticmethod
    def WritePageCode(code):
        with open('followersCode.html', mode='w', encoding='utf-8') as myfile:
            myfile.write(code)

    def GetFollowersFromAnotherAccount(self, account_id):
        self.driver.get(self.instagramURL + account_id)
        return self.GetFollowersCode()


def getFollowers(code):
    # subs_dir div.isgrP
    parser = bs(code, 'html.parser')
    all_subs = parser.select('div.PZuss')
    print(all_subs)


with open('followersCode.html', mode='r', encoding='utf-8') as sourceCode:
    code = sourceCode.read()
instagramBot = InstagramBot('ksiolove', 'vadim2001')
code = instagramBot.GetFollowersFromAnotherAccount('floridana.danaflo')
getFollowers(code)

time.sleep(1000)
