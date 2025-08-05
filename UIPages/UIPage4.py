from selenium.webdriver.common.by import By


class UIPage1:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.chitai-gorod.ru/"
        )

        self.driver.find_element(
            By.CLASS_NAME, "popmechanic-desktop").click()