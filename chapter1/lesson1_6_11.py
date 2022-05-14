from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration2.html"
browser = webdriver.Chrome()
browser.get(link)

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
# записываем в переменную welcome_text текст из элемента welcome_text_elt

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text
