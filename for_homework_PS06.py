import time
import csv
from os import write

from django.template.defaultfilters import title, pprint
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v85.fetch import continue_request
from urllib3.filepost import writer

driver = webdriver.Chrome()

url = ("https://www.ststroitel.ru/catalog/osveshchenie/lampy_svetodiodnye/")
driver.get(url)
time.sleep(30)
lamps = driver.find_elements(By.CSS_SELECTOR, "top-block-wrapper")
parsed_data = []
for lamp in lamps:
    try:
        title = lamp.find_elements(By.CSS_SELECTOR, "span.Ленты светодиодные").text
        company = lamp.find_elements(By.CSS_SELECTOR,"topic__heading").text

        price = lamp.find_elements(By.CSS_SELECTOR, "price_currency").text
        link = lamp.find_elements(By.CSS_SELECTOR, "a.scroll-to-top ROUND_COLOR PADDING" ).get_attribute("href")
    except:
        print("произошла ошибка при парсинге")
        continue
    parsed_data.append([title, company, price, link])
    driver.quit()
with open("ststroitel.csv", 'w',newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Название", "Производитель", "Цена", "Ссылка"])
    writer.writerows(parsed_data)
