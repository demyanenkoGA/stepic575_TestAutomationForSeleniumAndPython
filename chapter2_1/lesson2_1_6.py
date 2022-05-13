"""Метод get_attribute"""

import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link = "http://suninjuly.github.io/math.html"
calc = lambda x: str(math.log(abs(12 * math.sin(int(x)))))

with webdriver.Chrome() as browser:
    browser.get(link)
    # проверяем значение атрибута checked у people_radio
    people_radio = browser.find_element(By.ID, "peopleRule")
    people_checked = people_radio.get_attribute("checked")
    print("value of people radio: ", people_checked)
    assert people_checked is not None, "People radio is not selected by default"

    # проверяем значение атрибута checked у robots_radio
    robots_radio = browser.find_element(By.ID, "robotsRule")
    robots_checked = robots_radio.get_attribute("checked")
    print("value of robots_radio: ", robots_checked)
    assert robots_checked is None

    # проверяем значение атрибута disabled у кнопки Submit
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit: ", button_disabled)
    assert button_disabled is None

    # проверяем значение атрибута disabled у кнопки Submit после таймаута
    sleep(10)
    button_disabled = button.get_attribute("disabled")
    print("value of button Submit after 10sec: ", button_disabled)
    assert button_disabled is not None
