from selenium.webdriver.common.by import By
from chapter4_2.base_page import BasePage


class Main:
    URL = 'https://www.gosuslugi.ru/help/obratitsya_v_pos'
    LOGIN, PASSWORD = '4448@test.tst.pg18724', 'pr{{J@7|'

    btnEnter = (By.XPATH, '//button[text()="Войти"]')

    inputLogin = (By.XPATH, '//input[@id="login"]')
    inputPassword = (By.XPATH, '//input[@id="password"]')


class Func(BasePage):
    def auth(self):
        enter = self.browser.find_element(*Main.btnEnter)
        fieldLogin = self.browser.find_element(*Main.inputLogin)
        fieldLogin.send_keys(Main.LOGIN)
        fieldPassword = self.browser.find_element(*Main.inputPassword)
        fieldPassword.send_keys(Main.PASSWORD)
        enter.click()
