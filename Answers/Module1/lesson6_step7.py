from lesson6_step4 import close_browser
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Firefox()
    browser.get("http://suninjuly.github.io/huge_form.html")
    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Абоба")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    close_browser(browser)
