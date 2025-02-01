
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By

# Укажите путь к вашему веб-драйверу
driver_path = 'path/to/chromedriver'  # Замените на путь к вашему chromedriver
driver = webdriver.Chrome()

# URL сайта
url = 'https://divan.ru/'
driver.get(url)

# Подождите, пока загрузится страница
time.sleep(5)

# Найдите все нужные элементы (например, название и цену)
products = driver.find_elements(By.CLASS_NAME, 'product-card')  # Замените на актуальный класс

data = []

for product in products:
    title = product.find_element(By.CLASS_NAME, 'product-title').text  # Замените на актуальный класс
    price = product.find_element(By.CLASS_NAME, 'product-price').text  # Замените на актуальный класс
    data.append({'Title': title, 'Price': price})

# Закройте драйвер
driver.quit()

# Сохраните данные в CSV файл
df = pd.DataFrame(data)
df.to_csv('divan_data.csv', index=False, encoding='utf-8-sig')

print("Данные успешно сохранены в divan_data.csv.")
