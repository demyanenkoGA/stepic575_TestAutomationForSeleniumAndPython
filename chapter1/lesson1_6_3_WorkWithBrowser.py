"""Работа с браузером в Selenium"""

# №1
"""
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)
button = browser.find_element(By.ID, "submit_button")
button.click()

# закрываем браузер после всех манипуляций
browser.quit()
"""

# №2
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    button = browser.find_element(By.ID, "submit_button")
    button.click()

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()
"""

# №3
"""
with webdriver.Chrome() as browser:
    browser.get(link)
    button = browser.find_element(By.ID, "submit")
    button.click()
"""

# Best Practices
"""
with webdriver.Chrome() as browser:
    yield browser
"""
