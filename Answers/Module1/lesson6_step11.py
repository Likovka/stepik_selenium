from selenium import webdriver

from lesson6_step10 import insert_required_data

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Firefox()

insert_required_data(browser, link)

browser.quit()
