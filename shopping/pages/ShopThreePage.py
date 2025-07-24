import allure
from selenium.webdriver.common.by import By


class ShopThreePage:

    @allure.title("Нажатие на иконку корзину")
    @allure.feature("CLICK")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Нажатие на иконку 'Корзины'")
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(By.ID, "checkout").click()
