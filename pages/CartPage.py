import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CartPage:
        def __init__(self, driver):
            self.driver = driver
            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()
            self.driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie").click()
            self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()