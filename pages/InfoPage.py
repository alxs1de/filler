import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class InfoPage:
    def information(self, term):
        self.driver.find_element(By.ID, "first-name").send_keys(term)
        self.driver.find_element(By.ID, "last-name").send_keys(term)
        self.driver.find_element(By.ID, "postal-code").send_keys(term)
        self.driver.find_element(By.ID, "continue").click()