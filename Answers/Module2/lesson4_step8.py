from Answers.Module1.lesson6_step4 import close_browser
from lesson3_step4 import calc
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

try:
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Firefox()
    browser.get(link)

    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value.nowrap")
    browser.execute_script("return arguments[0].scrollIntoView(true);", x_element)
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.ID, "answer")
    input.send_keys(y)

    solve_btn = (browser.find_element(By.CSS_SELECTOR, "#solve.btn"))
    solve_btn.click()

finally:
    close_browser(browser)
