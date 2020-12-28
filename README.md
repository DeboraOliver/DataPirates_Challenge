# Data Pirates challenge

## Overview

Here you are going to find my answer to the Neoway's technical test.

I developed this project using a Linux (debian10) OS. Nonetheless, the only difference might be the pip freeze including a package called pkg-resources=0.0.0 which will not work.

## How to run it

Install a 3.x Python's version and Virtualenv:
<ol>
<li>Clone this repo : git clone https://github.com/DeboraOliver/DataPirates_Challenge.git</li>
<li>Go to that cloned repo : cd DataPirates_Challenge</li>
<li>Start a development environment using virtualenv ;</li>
<li>Install all dependencies : pip install -r requirements.txt;</li>
</ol>

## 1. Requirements

The main libraries used:

````
beautifulsoup4==4.9.3
certifi==2020.12.5
chardet==4.0.0
colorama==0.4.4
configparser==5.0.1
crayons==0.4.0
idna==2.10
numpy==1.19.4
pandas==1.1.5
python-dateutil==2.8.1
pytz==2020.5
requests==2.25.1
selenium==3.141.0
six==1.15.0
soupsieve==2.1
urllib3==1.26.2
webdriver-manager==3.2.2
````

## 2. How does it collect data

A bot accesses a given url using selenium and the data collecting part is done by BeautifulSoup. T

The last part is to gather information in only one dataframe and convert it to a jsonl file.

## 3. Further questions

### Which UFs is it using?

It is collecting data from 6 UFs: 

    ufs = ['AC','AL','AP','DF', 'RR','SE']

HOWEVER, it can capture information from any uf.

### Why does it need to include time gaps between commands?
To guarantee enough time to page load, the script might have:
  
    time.sleep(random.uniform(2.5, 4.5))
    
But you may find:
    
    menu_uf = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, '//*[@id="Geral"]/div/div/span[2]/label/select')))

### Why does it only use xpath where it might be good to use a link?

Xpath is highly changeable on social media and more popular websites. Due to the small risk of changes and the fact that this script is for a technical test, I personally decided to only use xpath, instead  of class/name/link.

## References

http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm
http://jsonlines.org
https://www.selenium.dev/exceptions/#stale_element_reference
https://github.com/NeowayLabs/jobs/blob/master/datapirates/challengePirates.md


