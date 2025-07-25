import allure
from selenium.webdriver.common.by import By


class ShopOnePage:

    @allure.description("Вход на сайт")
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.saucedemo.com/"
        )

    @allure.title("Ввод Имени")
    @allure.feature("ENTER")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Ввод имени 'standard_user'")
    def user(self, term):
        self.driver.find_element(By.ID, "user-name").send_keys(term)

    @allure.title("Ввод Пароля")
    @allure.feature("ENTER")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Ввод пароля 'secret_sauce'")
    def password(self, term):
        self.driver.find_element(By.ID, "password").send_keys(term)

    @allure.title("Нажатие на Логин")
    @allure.feature("CLICK")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Нажатие на кнопку логина")
    def login(self):
        self.driver.find_element(By.ID, "login-button").click()
