import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalcPage:


    @allure.title("Вход")
    @allure.feature("CHECK")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Вход на сайт, ожидание для прогрузки, увеличение размера окна")
    def __init__(self, driver):
        self._driver = driver
        with allure.step("Зайти на сайт"):
            self._driver.get(
                "https://bonigarcia.dev/selenium-webdriver-java/"
                "slow-calculator.html")
        with allure.step("Подождать 4 секунды"):
            self._driver.implicitly_wait(4)
        with allure.step("Увеличить размера окна"):
            self._driver.maximize_window()


    @allure.title("Установка Дэлея")
    @allure.feature("UPDATE")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Замена цифровых значений в поле ожидание на 45 и само ожидание (45 секунд)")
    def set_delay(self, wait):        # установка времени ожидания

        with allure.step("Проверка поля на доступ к вводу данных"):
            WebDriverWait(self._driver, wait).until(EC.element_to_be_clickable(
                (By.CSS_SELECTOR, "#delay")))

        with allure.step("Установка времени"):
            delay = "delay"
            self._driver.find_element(By.ID, delay).clear()
            self._driver.find_element(By.ID, delay).send_keys(wait)


    @allure.title("Нажатие на 7 + 8 =")
    @allure.feature("CREATE")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Нажатие на кнопки 7 + 8 =")
    def calculate(self, list_calc, wait):

        with allure.step("Нажатие на кнопки из списка и ожидание"):
            for button in list_calc:
                str = "//span[text()='" + button + "']"
                button_click = self._driver.find_element(By.XPATH, str)
                WebDriverWait(self._driver, wait).until(EC.element_to_be_clickable(
                    button_click))
                button_click.click()


    @allure.title("Число = 15")
    @allure.feature("CHECK")
    @allure.severity("Normal. Всё работает как надо")
    @allure.description("Удостоверение в том, что результата равен 15")
    def rezult_calc(self, rez, wait):

        with allure.step("Получение результатов и удостоверение в том что число равно 15"):
            WebDriverWait(self._driver, wait).until(
                EC.text_to_be_present_in_element(
                    (By.CSS_SELECTOR, '[class="screen"]'), rez))

            val = self._driver.find_element(
                By.CSS_SELECTOR, '[class="screen"]')
            rezult = float(val.text)
            return rezult

