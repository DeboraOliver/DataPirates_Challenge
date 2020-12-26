# import pandas as pd
# from urllib.request import urlopen as uReq
# from bs4 import BeautifulSoup as soup
import time, random, os, csv, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#import jsonl
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup


class DataPirates:

    def __init__(self):
        dirpath = os.getcwd ()
        chromepath = dirpath + '/assets/chromedriver.exe'

        # it will disable any unexpected notification
        chrome_options = webdriver.ChromeOptions ()
        prefs = {"profile.default_content_setting_values.notifications": 2}
        chrome_options.add_experimental_option ("prefs", prefs)
        self.driver = webdriver.Chrome (executable_path=chromepath, options=chrome_options)

        self.driver.get ('http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm')

        # self.search()


    def search(self):

        x = self.driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select')
        x.click()

        #let's get AL (Alagoas)
        select=Select(x)
        select.select_by_value("AL")

        self.driver.find_element_by_xpath('//*[@id="Geral"]/div/div/div[4]/input').click()

        time.sleep(random.uniform(2.5, 4.5))

        self.colecting_data()


    def colecting_data(self):

        current_url = self.driver.current_url

        self.uClient = uReq(current_url)
        self.page_html = self.uClient.read()
        self.uClient.close()  # fecha o pedido anterior qndo eu terminar

        # html parsing
        self.page_soup = soup(self.page_html, "html.parser")

        table = self.driver.find_element_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]')

        for row in table.find_elements_by_xpath('/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]/tbody'):
            print(row.text)


teste = DataPirates()


