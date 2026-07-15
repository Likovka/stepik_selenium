import math
import time

from Answers.Module1.lesson6_step4 import close_browser
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Firefox()
    browser.get(link)

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    time.sleep(1)

    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    close_browser(browser)
