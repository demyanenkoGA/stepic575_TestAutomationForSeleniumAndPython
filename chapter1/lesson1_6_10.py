"""Уникальность селекторов: часть 2"""

from selenium import webdriver
import time
from selenium.webdriver.common.by import By

with webdriver.Chrome() as browser:
    browser.get("http://suninjuly.github.io/registration1.html")

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('1')
    browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('1')
    browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('1')

    # Отправляем заполненную форму
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text
    time.sleep(10)

"""
try:
    link = "http://suninjuly.github.io/registration1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('1')
    browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('1')
    browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('1')
    # browser.find_element_by_xpath("//input[@placeholder = 'Введите имя']").send_keys('1')
    # browser.find_element_by_xpath("//input[@placeholder = 'Введите фамилию']").send_keys('1')
    # browser.find_element_by_xpath("//input[@placeholder = 'Введите Email']").send_keys('1')

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
"""