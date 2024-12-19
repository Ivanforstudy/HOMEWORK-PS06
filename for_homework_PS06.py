
import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Инициализация веб-драйвера
driver = webdriver.Chrome()

# URL для парсинга
url = "https://spb.hh.ru/vacancies/programmist"
driver.get(url)

# Использование WebDriverWait для ожидания загрузки вакансий
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "a.magritte-link")))

except TimeoutException:
    print("Элемент не найден на странице")
    driver.quit()
    exit()

# Находим все вакансии
vacancies = driver.find_elements(By.CLASS_NAME, "vacancy-info--ieHKDTkezpEj0Gsx")

parsed_data = []

# Парсинг информации о вакансиях
for vacancy in vacancies:
    try:
        title_element = vacancy.find_element(By.CSS_SELECTOR, ".vacancy-name-wrapper--PSD41i3dJDUNb5Tr")
        title = title_element.text

        company_element = vacancy.find_element(By.CSS_SELECTOR, ".company-name-badges-container--ofqQHaTYRFg0JM18")
        company = company_element.text

        salary_element = vacancy.find_element(By.CSS_SELECTOR, ".wide-container-magritte--TmgLMNxG7w8MIgQd")
        salary = salary_element.text

        link_element = vacancy.find_element(By.CSS_SELECTOR, "a.""magritte-link___b4rEM_4-3-14 ").text

    except Exception as e:
        print(f"Произошла ошибка при парсинге: {e}")
        continue

    parsed_data.append([title, company, salary, link])

# Закрываем драйвер
driver.quit()

# Сохраняем данные в CSV файл
with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)
