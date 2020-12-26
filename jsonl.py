import os
import dload
import pandas as pd

def json(url):


    #getting its location
    dirpath = os.getcwd()
    raw_data = dirpath + "\datapirates.csv"

    #putting all data into a dataframe and creating a new column for series_id
    df = pd.read_csv(raw_data)
    df['series_id'] = df['Localidade'] + '-' + df['Faixa de CEP'].map(str)

    #creating a NDJson also known as Json Line
    df.to_json('JsonResult.json', orient = 'records', lines = True)

if __name__ == '__main__':
    url = "https://www.jodidata.org/_resources/files/downloads/gas-data/jodi_gas_csv_beta.zip"
    json(url)