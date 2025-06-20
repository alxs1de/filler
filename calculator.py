from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from pages.CalcPage import CalcPage

def test_calc():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    delay_button = CalcPage(browser)
    delay_button.delay('45')

    calc_buttons = CalcPage(browser)
    calc_buttons.calculator()

    results = CalcPage(browser)
    results.result()

    quit_ = CalcPage(browser)
    quit_.quit()
