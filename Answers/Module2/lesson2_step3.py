from Answers.Module1.lesson6_step4 import close_browser
from selenium import webdriver
from selenium.webdriver.common.by import By


def calc(first, second):
  return str(int(first) + int(second))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Firefox()
    browser.get(link)

    a_element = browser.find_element(By.ID, "num1")
    b_element = browser.find_element(By.ID, "num2")
    a_num = a_element.text
    b_num = b_element.text
    answer = calc(a_num, b_num)

    browser.find_element(By.ID, "dropdown").click()
    browser.find_element(By.CSS_SELECTOR, f"[value='{answer}']").click()

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    close_browser(browser)
