import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def insert_required_data(driver, current_link):
    driver.get(current_link)
    # Выбор всех обязательных полей и их заполнение
    first_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your first name'][required]")
    last_name = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your last name'][required]")
    email = driver.find_element(By.CSS_SELECTOR, "input[placeholder='Input your email'][required]")
    fields = [first_name, last_name, email]
    for field in fields:
        field.send_keys("абоба")

    button = driver.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Загрузка страницы
    time.sleep(1)

    welcome_text_elt = driver.find_element(By.TAG_NAME, "h1")
    welcome_text = welcome_text_elt.text

    assert "Congratulations! You have successfully registered!" == welcome_text


if __name__ == "__main__":
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Firefox()

    insert_required_data(browser, link)

    browser.quit()
