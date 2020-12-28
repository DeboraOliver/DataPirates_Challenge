# Data Pirates challenge

Here you are going to find my answer to the Neoway's technical test.


## Overview


## How to use it

Install a 3.x Python's version and Virtualenv:
<ol>
<li>Clone this repo : git clone https://github.com/DeboraOliver/DataPirates_Challenge.git</li>
<li>Go to that cloned repo : cd DataPirates_Challenge</li>
<li>Start a development environment: virtualenv --python $( which python3 ) py3;</li>
<li>Install all dependencies : pip install -r requirements.txt;</li>
</ol>

## 1. Why am I using two scripts?

It was a personal decision to turn thins clear and a little more organized.

The first script named core.py uses a given url to access and collect data. The information collected (<i>localidade</i> and <i>faixa de cep</i>). The second script is called tojson.py. It simply transform the data in a dataframe and then, in a beautiful json file. Therefore, they complement one another.

## 2. Requirements

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
The tojson.py uses:

```

```

