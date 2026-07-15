import math
import time

from Answers.Module1.lesson6_step4 import close_browser
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


def accept_alert(driver):
    driver.switch_to.alert.accept()
    time.sleep(1)


def switch(driver, specific_func):
    try:

        button = driver.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        specific_func(driver)

        x_element = driver.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
        x = x_element.text
        y = calc(x)

        input = driver.find_element(By.ID, "answer")
        input.send_keys(y)

        submit = driver.find_element(By.CSS_SELECTOR, "button.btn")
        submit.click()

    finally:
        close_browser(driver)


if __name__ == '__main__':
    link = "http://suninjuly.github.io/alert_accept.html"

    browser = webdriver.Firefox()
    browser.get(link)

    switch(browser, accept_alert)
