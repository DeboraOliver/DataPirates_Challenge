import pandas as pd
import time, random
from selenium import webdriver
from selenium.webdriver.support.select import Select
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DataPirates:

    def __init__(self,driver, url, uf, raw_localidade, raw_faixa_cep, estado):

        self.driver = driver
        self.url = url
        self.uf = uf
        self.raw_localidade = raw_localidade
        self.raw_faixa_cep = raw_faixa_cep
        self.estado = estado

        self.driver.get(self.url)

        self.search()

    def search(self):

        menu_uf = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/select')))

        menu_uf.click()

        #let's get uf
        select=Select(menu_uf)
        select.select_by_value(self.uf)

        self.driver.find_element_by_xpath('//*[@id="Geral"]/div/div/div[4]/input').click()

        time.sleep(random.uniform(2.5, 4.5))

        self.colecting_data()

    def colecting_data(self):

        current_url = self.driver.current_url

        self.uClient = uReq(current_url)
        self.page_html = self.uClient.read()
        self.uClient.close()

        # html parsing
        self.page_soup = soup(self.page_html, "html.parser")

        #first page table
        table = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table[2]')
        #any other page
        table1 = self.driver.find_element_by_xpath(
            '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/table')

        i=50
        while i>=2:
            for cidade in table.find_elements_by_xpath('.//tbody/tr[{0}]/td[1]'.format(i)):
                self.raw_localidade.append(cidade.text)
                self.estado.append(self.uf)
                for cep in table.find_elements_by_xpath('.//tbody/tr[{0}]/td[2]'.format(i)):
                    self.raw_faixa_cep.append(cep.text)
            i -= 1

        proxima_pagina = '/html/body/div[1]/div[3]/div[2]/div/div/div[2]/div[2]/div[2]/div[2]/a'

        try:
            while proxima_pagina is not None:
                j = 51
                while j >= 2:
                    self.driver.find_element_by_xpath(proxima_pagina).click()
                    time.sleep(random.uniform(5.5, 6.5))
                    for local in table1.find_elements_by_xpath('.//tbody/tr[{0}]/td[1]'.format(j)):
                        print(j)
                        print(local.text)
                        self.raw_localidade.append(local.text)
                        self.estado.append(self.uf)
                        for ceps in table1.find_elements_by_xpath('.//tbody/tr[{0}]/td[2]'.format(j)):
                            print(ceps.text)
                            self.raw_faixa_cep.append(ceps.text)
                    j -= 1

        except:
            print("Não há próxima pagina")
            #NOVA PESQUISA
            self.driver.get(self.url)


if __name__ == "__main__":

    url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm'
    ufs = ['AC','AL','AP','DF', 'RR','SE']

    raw_localidade = []
    raw_faixa_cep = []
    estado =[]

    driver = webdriver.Chrome(ChromeDriverManager().install())

    for uf in ufs:
        data = DataPirates(driver, url, uf, raw_localidade, raw_faixa_cep, estado)

    df = pd.DataFrame(data={"Localidade": raw_localidade,"UF": estado, "Faixa de CEP": raw_faixa_cep})
    df.drop_duplicates(subset ="Faixa de CEP", keep = 'first', inplace = True)
    df.sort_values(by=['Localidade', 'UF'], ascending=True)
    #add id
    df['id'] = pd.RangeIndex(stop=df.shape[0])

    #reordering columns
    df = pd.DataFrame(df, columns=['id', 'Localidade', 'UF', 'Faixa de CEP'])

    print(df)

    df_list = []
    df_list.append(df)

    with open("final_result.jsonl", 'w', encoding='utf-8') as file:
        df.to_json(file, force_ascii=False,orient="records",
               lines=True)

    driver.quit()







