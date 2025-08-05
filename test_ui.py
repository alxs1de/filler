from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pytest
import allure

from UIPages.UIPage1 import UIPage1
# from UIPages.UIPage2 import UIPage2
# from UIPages.UIPage3 import UIPage3
# from UIPages.UIPage4 import UIPage4
# from UIPages.UIPage5 import UIPage5

def test_shop():
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )

    # Корзина
    cart = UIPage1(browser)