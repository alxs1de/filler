import allure
from selenium.webdriver.common.by import By


class ShopTwoPage:

    @allure.title("Добавка товаров и нажатие на иконку корзины")
    @allure.feature("CLICK")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Нажатие на кнопки 'Add to cart' у 'Backpack', 'Bolt T-Shirt', 'Onesie' и на иконку корзины")
    def __init__(self, driver):
        self.driver = driver
        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-backpack").click()

        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt").click()

        self.driver.find_element(
            By.ID, "add-to-cart-sauce-labs-onesie").click()

        self.driver.find_element(
            By.CLASS_NAME, "shopping_cart_link").click()
