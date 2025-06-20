from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.LoginPage import LoginPage
from pages.CartPage import CartPage
from pages.CheckoutPage import CheckoutPage
from pages.InfoPage import InfoPage
from pages.QuitPage import QuitPage

def test_shop():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    login_page = LoginPage(browser)
    login_page.user("standard_user")
    login_page.password("secret_sauce")
    login_page.login()

    cart_page = CartPage(browser)
    cart_page.__init__()

    checkout_ = CheckoutPage(browser)
    checkout_.checkout()

    info = InfoPage(browser)
    info.information("Ivan", "Petrov", "123456", ())

    quit_ = QuitPage(browser)
    quit_.quit()