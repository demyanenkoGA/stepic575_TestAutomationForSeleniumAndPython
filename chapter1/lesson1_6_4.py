"""Задание: поиск элементов с помощью Selenium"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # input1 = browser.find_element_by_tag_name(value1)
    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")

    # input2 = browser.find_element_by_name(value2)
    input2 = browser.find_element(By.NAME, "last_name")
    input2.send_keys("Petrov")

    # input3 = browser.find_element_by_class_name(value3)
    input3 = browser.find_element(By.CLASS_NAME, "city")
    input3.send_keys("Smolensk")

    # input4 = browser.find_element_by_id(value4)
    input4 = browser.find_element(By.ID, "country")
    input4.send_keys("Russia")

    # button = browser.find_element_by_css_selector("button.btn")
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла

"""
with webdriver.Chrome() as browser:
    browser.get(link)
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
    time.sleep(30)
"""