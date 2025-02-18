import requests
from bs4 import BeautifulSoup

with open('index.html') as html:
    soup_soup = BeautifulSoup(html, 'html.parser')

    print(soup_soup.h1)

url = "https://beautiful-soup-4.readthedocs.io/en/latest/"

response = requests.get(url)
response.raise_for_status()

ramen_soup = BeautifulSoup(response.content, "html.parser")

h1s = ramen_soup.find_all('h1s')
titles = [ h1.text for h1 in h1s ]

# SCRAPE AMAZON WITH SELENIUM

url = "https://www.amazon.com/stores/page/6B079A31-BE2A-4F99-A1C3-A3BFACEE1FF2/?_encoding=UTF8&channel=SB_Gwayresort&pd_rd_w=SFCo0&content-id=amzn1.sym.fe5cecb5-cf45-41da-b21f-260024eccff6&pf_rd_p=fe5cecb5-cf45-41da-b21f-260024eccff6&pf_rd_r=K5VZN063DPCXDCXXHEY7&pd_rd_wg=ZJ1zZ&pd_rd_r=827fc454-cb77-429a-81f6-6eea1d3302bc&ref_=pd_hp_d_btf_unk"

# ################THIS DOESNT WORK#############################
# response = requests.get(url)
# response.raise_for_status()

# amazon_soup = BeautifulSoup(response.content, "html.parser")
###############################################################

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service

# the configuration here will depend on your OS and browser setup
service = Service("/snap/bin/firefox.geckodriver") 

options = Options()

options.headless = True

driver = webdriver.Firefox( service=service)
driver.get(url)
h1 = driver.find_element(By.TAG_NAME, 'h1')
print(h1)
driver.close()