"""Задание: поиск сокровища с помощью get_attribute"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/get_attribute.html"
calc = lambda x: str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)
    x_treasure = browser.find_element(By.ID, 'treasure').get_attribute('valuex')
    result = calc(x_treasure)
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
    browser.find_element(By.XPATH, '//input[@id="robotCheckbox"]').click()
    browser.find_element(By.XPATH, '//input[@id="robotsRule"]').click()
    browser.find_element(By.XPATH, '//button[@class="btn btn-default"][not(@disabled="disabled")]').click()

    alert = browser.switch_to.alert
    print(alert.text)
