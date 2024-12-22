
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Запускаем драйвер
driver = webdriver.Chrome()  # Убедитесь, что у вас установлен драйвер Chrome
url = "https://www.ozon.ru/category/naushniki-15547/?category_was_predicted=true&deny_category_prediction=true&from_global=true&text=%D0%BD%D0%B0%D1%83%D1%88%D0%BD%D0%B8%D0%BA%D0%B8+%D0%B1%D0%B5%D1%81%D0%BF%D1%80%D0%BE%D0%B2%D0%BE%D0%B4%D0%BD%D1%8B%D0%B5/"
driver.get(url)

# Используем явное ожидание
try:
    WebDriverWait(driver, 10).until \
        (EC.presence_of_all_elements_located((By.CLASS_NAME, "bq010-a bq010-a4 bq010-a6 i7x_23")))
except Exception as e:
    print(f"Ошибка ожидания загрузки элементов: {e}")
    driver.quit()
    exit()

gadgets = driver.find_elements(By.CLASS_NAME, "bq010-a bq010-a4 bq010-a6 i7x_23")
print(f"Найдено элементов: {len(gadgets)}")
parsed_data = []

for gadget in gadgets:
    try:
        title_element = gadget.find_element(By.CSS_SELECTOR, "span.tsBody500medium")
        title = title_element.text

        company_element = gadget.find_element(By.CSS_SELECTOR, "span.p6b06-04")
        company = company_element.text

        price_element = gadget.find_element(By.CSS_SELECTOR, "span.c3023-a1.tsHeadline500medium.c3023-b1c3023a6")
        price = price_element.text

        link_element = gadget.find_element(By.CSS_SELECTOR, "a")
        link = link_element.get_attribute("href")

        parsed_data.append([title, company, price, link])
    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")

with open("ozon.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название гаджета', 'Название компании', 'Цена', 'Ссылка на рекламу'])
    writer.writerows(parsed_data)

print("Парсинг завершен, данные сохранены в ozon.csv")
driver.quit()

