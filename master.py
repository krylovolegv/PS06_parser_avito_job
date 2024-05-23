# Импортируем модуль со временем
import time
# Импортируем модуль csv
import csv
# Импортируем Selenium
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By

# Установка geckodriver
service = FirefoxService(executable_path=GeckoDriverManager().install())

# Создаём объект браузера, через который мы будем действовать.
driver = webdriver.Firefox(service=service)

# В отдельной переменной указываем сайт, который будем просматривать
url = "https://www.avito.ru/kaliningrad/vakansii/iurist-ASgBAgICAUTUzBHo7YYD"

# Открываем веб-страницу
driver.get(url)

# Задаём 5 секунд ожидания, чтобы веб-страница успела прогрузиться
time.sleep(5)

# Перезагружаем веб-страницу
driver.refresh()

# Задаём 10 секунд ожидания, чтобы веб-страница успела прогрузиться после перезагрузки
time.sleep(10)

# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'iva-item-root-_lk9K')

# Проверяем, что вакансии найдены
if vacancies:
    print(f"Найдено вакансий: {len(vacancies)}")
    # Выводим вакансии на экран
    # for vacancy in vacancies:
    #     title_element = vacancy.find_element(By.CLASS_NAME, 'styles-module-root-GKtmM')  # Обновите селектор, если необходимо
    #     title = title_element.text if title_element else "Не удалось получить название"
    #     print(f"Вакансия: {title}")
else:
    print("Вакансий не найдено.")

# Закрываем браузер
driver.quit()
