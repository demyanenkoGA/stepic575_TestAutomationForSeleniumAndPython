"""Задание: поиск элемента по тексту в ссылке"""

import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

link_text = str(math.ceil(math.pow(math.pi, math.e)*10000))
link = "http://suninjuly.github.io/find_link_text"

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.LINK_TEXT, link_text).click()
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(30)
