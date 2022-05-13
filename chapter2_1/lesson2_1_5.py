"""Задание: кликаем по checkboxes и radiobuttons (капча для роботов)"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/math.html"
calc = lambda x: str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)
    x_value = browser.find_element(By.XPATH, '//span[@id="input_value"]').text
    result = calc(x_value)
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)

    browser.find_element(By.XPATH, '//label[@for="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//label[@for="robotsRule"]').click()
    browser.find_element(By.XPATH, '//button[@class="btn btn-default"][not(@disabled="disabled")]').click()
    sleep(10)
