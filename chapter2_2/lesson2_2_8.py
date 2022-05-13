"""Задание: загрузка файла"""

import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from collections import namedtuple

user_tuple = namedtuple('DATA', 'name lastname email')
current_dir = os.path.abspath(os.path.dirname(__file__))


link = 'http://suninjuly.github.io/file_input.html'
user = user_tuple('Иван', 'Иванов', 'test@test.com')
file_path = os.path.join(current_dir, 'testfile.txt')

with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.XPATH, '//input[@name="firstname"]').send_keys(user.name)
    browser.find_element(By.XPATH, '//input[@name="lastname"]').send_keys(user.lastname)
    browser.find_element(By.XPATH, '//input[@name="email"]').send_keys(user.email)
    browser.find_element(By.XPATH, '//input[@id="file"]').send_keys(file_path)
    browser.find_element(By.XPATH, '//button[@class="btn btn-primary"][not(@disabled="disabled")]').click()

    alert = browser.switch_to.alert
    print(alert.text.split(': ')[-1])
