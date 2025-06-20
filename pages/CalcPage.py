import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class CalcPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    def delay(self, term):
        self.driver.find_element(By.ID, "delay").clear()
        self.driver.find_element(By.ID, "delay").send_keys(term)

    def calculator(self):
        self.driver.find_element(By.XPATH, "//span[text()='7']").click()
        self.driver.find_element(By.XPATH, "//span[text()='+']").click()
        self.driver.find_element(By.XPATH, "//span[text()='8']").click()
        self.driver.find_element(By.XPATH, "//span[text()='=']").click()

    def result(self):
        result = WebDriverWait(self.driver, 45).until(
        EC.text_to_be_present_in_element((By.CLASS_NAME, "screen"), "15")
    )
    assert result

    def quit(self):
        self.driver.quit()
