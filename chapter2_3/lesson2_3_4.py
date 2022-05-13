"""Задание: принимаем alert"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By

link = 'http://suninjuly.github.io/alert_accept.html'
calc = lambda x: str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"][not(@disabled="disabled")]').click()
    alert = browser.switch_to.alert
    alert.accept()

    result = calc(int(browser.find_element(By.XPATH, '//span[@id="input_value"]').text))
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"][not(@disabled="disabled")]').click()

    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
