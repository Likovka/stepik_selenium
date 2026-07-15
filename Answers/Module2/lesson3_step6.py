import time

from lesson3_step4 import switch
from selenium import webdriver


def switch_to_window(driver):
    driver.switch_to.window(driver.window_handles[1])
    time.sleep(1)


link = "http://suninjuly.github.io/redirect_accept.html"

browser = webdriver.Firefox()
browser.get(link)
switch(browser, switch_to_window)
