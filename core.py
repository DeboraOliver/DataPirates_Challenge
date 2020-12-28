import pandas as pd
import time, random, os, csv, datetime
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#import jsonl
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tojsonl


class DataPirates:

    def __init__(self, url):

        self.url = url
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

        self.driver.get (url)

        self.search()


    def search(self):
        try:

            menu_uf = self.driver.find_element_by_xpath('//*[@id="Geral"]/div/div/span[2]/label/select')
            time.sleep(random.uniform(2, 3))

        except: #vamos inicializar  usando outro driver em caso de problemas
            self.driver.quit()

            print("We've got a problem with GoogleDriver! Let's try something even better")
            self.driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())

            self.driver.get(self.url)
            menu_uf = WebDriverWait(self.driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/select')))

        menu_uf.click()


        #let's get AC
        select=Select(menu_uf)
        select.select_by_value("MG")

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

        #first page table
        table = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]')
        #any other page
        table1 = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table')

        self.raw_localidade = []
        self.raw_faixa_cep = []

        i=51
        while i>=2:
            for cidade in table.find_elements_by_xpath('.//tbody/tr[{0}]/td[1]'.format(i)):
                self.raw_localidade.append(cidade.text)
                for cep in table.find_elements_by_xpath('.//tbody/tr[{0}]/td[2]'.format(i)):
                    self.raw_faixa_cep.append(cep.text)
            i -= 1

        proxima_pagina = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/a'

        j = 49

        while proxima_pagina is not None:
            while j >= 2:
                try:
                    self.driver.find_element_by_xpath(proxima_pagina).click()
                    for cidade in table1.find_elements_by_xpath('.//tbody/tr[{0}]/td[1]'.format(j)):
                        print(j)
                        print(cidade.text)
                        self.raw_localidade.append(cidade.text)
                        for cep in table1.find_elements_by_xpath('.//tbody/tr[{0}]/td[2]'.format(j)):
                            print(cep.text)
                            self.raw_faixa_cep.append(cep.text)
                    j -= 1

                except:
                    print("There's not next page")
                    pass

                finally:
                    print(len(self.raw_localidade))

        print(self.raw_localidade)
        print(self.raw_faixa_cep)



        #self.driver.quit()

if __name__ == "__main__":

    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    ufs = ['MG', 'SC']

    teste = DataPirates(url)
    # for uf in ufs:
    #     search(url, uf)

#quando não tem proximapagina
#/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]
#quando tem
#/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/a


