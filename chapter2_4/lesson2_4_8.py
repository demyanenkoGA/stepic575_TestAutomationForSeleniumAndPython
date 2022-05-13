"""Задание: ждем нужный текст на странице"""

import math
import pyperclip
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = 'http://suninjuly.github.io/explicit_wait2.html'
calc = lambda x: str(math.log(abs(12 * math.sin(x))))


with webdriver.Chrome() as browser:
    browser.get(link)
    WebDriverWait(browser, 13).until(EC.text_to_be_present_in_element((By.ID, 'price'), '$100'))
    browser.find_element(By.ID, 'book').click()

    result = calc(int(browser.find_element(By.XPATH, '//span[@id="input_value"]').text))
    browser.find_element(By.XPATH, '//input[@id="answer"]').send_keys(result)
    browser.find_element(By.ID, 'solve').click()

    alert = browser.switch_to.alert
    addToClipBoard = alert.text.split(': ')[-1]
    pyperclip.copy(addToClipBoard)
