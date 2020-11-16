import requests
import time
from bs4 import BeautifulSoup

URL = 'https://www.bestbuy.ca/en-ca/product/logitech-g915-tkl-lightspeed-wireless-backlit-mechanical-linear-gaming-keyboard-carbon-english/14662052'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
time.sleep(3)
title = soup.find("h1", {"class": "productName_19xJx"}).text
price = soup.find("div", {"class": "price_FHDfG large_3aP7Z"}).text

converted_price = int(price[1:4])
print(title)
if converted_price < 300:   
    print(converted_price)
    print("Buy now!")
else:
    print("Regular price")
