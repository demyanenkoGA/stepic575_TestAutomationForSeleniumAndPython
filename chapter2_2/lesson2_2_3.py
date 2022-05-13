"""Задание: работа с выпадающим списком"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

link1 = 'http://suninjuly.github.io/selects1.html'
link2 = 'http://suninjuly.github.io/selects2.html'

link = link2

with webdriver.Chrome() as browser:
    browser.get(link)
    result = str(int(browser.find_element(By.XPATH, '//span[@id="num1"]').text) + int(browser.find_element(By.XPATH, '//span[@id="num2"]').text))
    Select(browser.find_element(By.TAG_NAME, "select")).select_by_visible_text(result)
    browser.find_element(By.XPATH, '//button[@class="btn btn-default"][not(@disabled="disabled")]').click()

    alert = browser.switch_to.alert
    print(alert.text)
