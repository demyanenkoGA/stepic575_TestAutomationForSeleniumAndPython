import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

link1 = 'http://suninjuly.github.io/registration1.html'
link2 = 'http://suninjuly.github.io/registration2.html'


def registration(link):
    with webdriver.Chrome() as browser:
        browser.get(link)
        browser.find_element(By.XPATH, '//input[@placeholder="Input your first name"]').send_keys('1')
        browser.find_element(By.XPATH, '//input[@placeholder="Input your last name"]').send_keys('1')
        browser.find_element(By.XPATH, '//input[@placeholder="Input your email"]').send_keys('1')

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        sleep(1)
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        return welcome_text


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        self.assertEqual(registration(link1), "Поздравляем! Вы успешно зарегистировались!", "registration is failed")

    def test_reg2(self):
        self.assertEqual(registration(link2), "Поздравляем! Вы успешно зарегистировались!", "registration is failed")


if __name__ == "__main__":
    unittest.main()
