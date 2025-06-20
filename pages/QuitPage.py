import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

class QuitPage:
    def quit(self):
        result = self.driver.find_element(By.CLASS_NAME, "summary_total_label").text
        assert result == "Total: $58.29"
        self.driver.quit()