from main_page import MainPage
from login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com"
    page = MainPage(browser, link)
    page.open()
    page.go_to_login_page()
    print(browser.get_log("Network"))
    login_page = LoginPage(browser, browser.current_url)
    for entry in browser.get_log('browser'):
        print(entry)
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    for entry in browser.get_log('browser'):
        print(entry)
    page.should_be_login_link()



"""pytest -v --tb=line --language=en test_main_page.py"""
"""http://selenium1py.pythonanywhere.com/ru/accounts/login/"""
