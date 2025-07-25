import allure
from selenium.webdriver.common.by import By


class ShopFivePage:

    @allure.title("Проверка цены")
    @allure.feature("CHECK")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Удостоверение того, что цена равна $58.29")
    def __init__(self, driver):

        self.driver = driver
        result = self.driver.find_element(
            By.CLASS_NAME, "summary_total_label").text
        assert result == "Total: $58.29"
        self.driver.quit()
