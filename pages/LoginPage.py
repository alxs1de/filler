import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/"
        )

    def user(self, term):
            self.driver.find_element(By.ID, "user-name").send_keys(term)
    def password(self, term):
            self.driver.find_element(By.ID, "password").send_keys(term)
    def login(self):
            self.driver.find_element(By.ID, "login-button").click()
