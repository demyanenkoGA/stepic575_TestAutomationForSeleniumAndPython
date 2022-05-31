# from chapter4_2.main_page import MainPage
from pages import Main, Func
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

URL = 'https://www.gosuslugi.ru/help/obratitsya_v_pos'

"""
def test_guest_can_go_to_login_page(browser):
    link = Main.URL
    page = MainPage(browser, link)
    page.open()
    Func.auth()
    sleep(60)
"""
with webdriver.Chrome() as browser:
    browser.get(URL)
    sleep(10)
    btnEnter = browser.find_element(By.XPATH, '//button[text()="Войти"]')
    browser.find_element(By.XPATH, '//input[@id="login"]').send_keys(Main.LOGIN)
    browser.find_element(By.XPATH, '//input[@id="password"]').send_keys(Main.PASSWORD)
    btnEnter.click()
    sleep(600)
