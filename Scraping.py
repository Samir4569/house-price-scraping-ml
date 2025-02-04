from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from bs4 import BeautifulSoup
import requests
import pandas as pd


chrome_options = Options()
service = Service('C:/Users/Samir/Downloads/chromedriver-win32/chromedriver-win32/chromedriver.exe')
driver = webdriver.Chrome(service=service, options=chrome_options)

for i in range(1, 100):
    driver.get(f'https://bina.az/baki/alqi-satqi/menziller?page={i}')
    with open (f'Pages/open{i}.html', 'w', encoding='utf-8') as file:
        file.write(driver.page_source)
driver.quit()

datas = []

for i in range(1, 100):
    with open(f'Pages/open{i}.html', 'r', encoding='utf-8') as file:
        content = file.read()
        soup = BeautifulSoup(content, 'lxml')
        cards = soup.find_all('div', class_='card_params')

    for j in range(len(cards)):
        price = cards[j].find('div', class_='price').text if cards[j].find('div', class_='price') else None
        location = cards[j].find('div', class_='location').text if cards[j].find('div', class_='location') else None
        detail = cards[j].find('ul', class_='name').text if cards[j].find('ul', class_='name') else None
        
        datas.append({
            'price': price,
            'location': location,
            'detail': detail
        })


df = pd.DataFrame(datas)

df.to_csv('House.csv', index=False)
