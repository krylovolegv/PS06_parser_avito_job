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

# Задаём 10 секунд ожидания, чтобы веб-страница успела прогрузиться
time.sleep(10)

# Находим все карточки с вакансиями с помощью названия класса
# Названия классов берём с кода сайта
vacancies = driver.find_elements(By.CLASS_NAME, 'iva-item-root-_lk9K')

# Выводим вакансии на экран
for vacancy in vacancies:
    print(vacancy.text)

# Закрываем браузер
driver.quit()
