import os
import time

from Answers.Module1.lesson6_step4 import close_browser
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Firefox()
    browser.get(link)

    firstname = browser.find_element(By.NAME, "firstname")
    firstname.send_keys("Валера")

    lastname = browser.find_element(By.NAME, "lastname")
    lastname.send_keys("Валеров")

    lastname = browser.find_element(By.NAME, "email")
    lastname.send_keys("valera@mail.ru")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    file_element = browser.find_element(By.ID, "file")
    file_element.send_keys(file_path)

    time.sleep(1)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    close_browser(browser)
