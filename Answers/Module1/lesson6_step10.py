import time

from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    # Выбор всех обязательных полей и их заполнение
    elements = browser.find_elements(By.XPATH, "//label[contains(.,'*')]/following-sibling::input")
    for element in elements:
        element.send_keys("Абоба")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Загрузка страницы
    time.sleep(1)

    welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    browser.quit()
