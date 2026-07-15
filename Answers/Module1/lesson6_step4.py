from selenium import webdriver
from selenium.webdriver.common.by import By


def input_value(driver):
    try:
        input1 = driver.find_element(By.TAG_NAME, "input")
        input1.send_keys("Ivan")
        input2 = driver.find_element(By.NAME, "last_name")
        input2.send_keys("Petrov")
        input3 = driver.find_element(By.CLASS_NAME, "form-control.city")
        input3.send_keys("Smolensk")
        input4 = driver.find_element(By.ID, "country")
        input4.send_keys("Russia")
        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

    finally:
        close_browser(driver)


def close_browser(driver):
    alert = driver.switch_to.alert
    print(alert.text[alert.text.rfind(':') + 2:])
    alert.accept()

    driver.close()
    driver.quit()


if __name__ == "__main__":
    link = "http://suninjuly.github.io/simple_form_find_task.html"

    browser = webdriver.Firefox()
    browser.get(link)

    input_value(browser)
