"""Задание на execute_script"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

link = 'http://suninjuly.github.io/execute_script.html'
calc = lambda x: str(math.log(abs(12 * math.sin(x))))


def scroll_to_element(browser, element, click=False, send=None):
    browser.execute_script('return arguments[0].scrollIntoView(true);', element)
    if click:
        element.click()
    if send:
        element.send_keys(send)


with webdriver.Chrome() as browser:
    browser.get(link)
    var_x = int(browser.find_element(By.XPATH, '//span[@id="input_value"]').text)
    result = calc(var_x)
    scroll_to_element(browser, browser.find_element(By.ID, 'answer'), send=result)
    scroll_to_element(browser, browser.find_element(By.ID, 'robotCheckbox'), click=True)
    scroll_to_element(browser, browser.find_element(By.ID, 'robotsRule'), click=True)
    scroll_to_element(browser, browser.find_element(By.XPATH, '//button[@class="btn btn-primary"][not(@disabled="disabled")]'), click=True)

    alert = browser.switch_to.alert
    print(alert.text)
