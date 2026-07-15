import math

from lesson6_step4 import input_value
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/find_link_text"
browser = webdriver.Firefox()
browser.get(link)

value = str(math.ceil(math.pow(math.pi, math.e) * 10000))
answer = browser.find_element(By.LINK_TEXT, value)
answer.click()

input_value(browser)
