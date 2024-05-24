import time
import csv
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Установка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Создаём объект браузера, через который мы будем действовать
driver = webdriver.Firefox(service=service)

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://kaliningrad.hh.ru/vacancies/yurist"

# Открываем веб-страницу
driver.get(url)

# Задаём 5 секунд ожидания, чтобы веб-страница успела прогрузиться
time.sleep(5)

# Перезагружаем веб-страницу
driver.refresh()

# Ждем, пока загрузится хотя бы один элемент вакансии (до 10 секунд)
try:
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'serp-item')))
except Exception as e:
    print(f"Страница не загрузилась: {e}")
    driver.quit()
    exit()

# Находим все карточки с вакансиями с помощью названия класса
vacancies = driver.find_elements(By.CLASS_NAME, 'serp-item')

# Проверяем, что вакансии найдены
if vacancies:
    print(f"Найдено вакансий: {len(vacancies)}")
else:
    print("Вакансий не найдено.")
    driver.quit()
    exit()

# Создаём список, в который потом всё будет сохраняться
parsed_data = []

# Функция для извлечения текста с обработкой ошибок
def safe_find_element_text(vacancy, by, value):
    try:
        return vacancy.find_element(by, value).text
    except Exception as e:
        print(f"Ошибка при парсинге элемента {value}: {e}")
        return "Не найдено"

# Перебираем коллекцию вакансий
for vacancy in vacancies:
    try:
        # Находим элементы внутри вакансий по значению, используя CSS-селекторы
        title = vacancy.find_element(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        company = vacancy.find_element(By.CSS_SELECTOR, 'span.company-info-text--O32pGCRW0YDmp3BHuNOP').text
        salary = vacancy.find_element(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_element(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except Exception as e:
        print(f"Произошла ошибка при парсинге вакансии: {e}")
        continue

    # Вносим найденную информацию в список
    parsed_data.append([title, company, salary, link])

# Закрываем подключение браузера
driver.quit()

# Прописываем открытие нового файла, задаём ему название и форматирование
with open("hh_vacancies.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'Название компании', 'Зарплата', 'Ссылка на вакансию'])
    writer.writerows(parsed_data)

# Выводим сообщение о завершении
print("Данные успешно сохранены в hh_vacancies.csv")


