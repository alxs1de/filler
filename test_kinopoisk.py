import pytest
from selenium import webdriver  # импорт драйвера для взаимодействия с браузером
from selenium.webdriver.common.by import By
import allure

@pytest.fixture()
def chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(300)
    driver.maximize_window()
    yield driver
    driver.quit()

@allure.title("Поиск фильма по названию")
@allure.description("Вход на страницу фильма, выбор фильма")
@allure.severity("normal")
def test_search(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("Остров")
    chrome.find_element(By.ID, "suggest-item-film-397667").click()
    assert chrome.find_element(By.CSS_SELECTOR, "span[data-tid='75209b22']").text == "Остров проклятых (2009)"


@allure.title("Поиск фильма по символам")
@allure.description("Ввод в поисковую страку символов")
@allure.severity("normal")
def test_negative(chrome):
    chrome.get("https://www.kinopoisk.ru/")
    chrome.find_element(By.NAME, "kp_query").send_keys("@!%")
    assert chrome.find_element(By.XPATH, "//*[contains(@class, 'emptySuggest')]").text == "По вашему запросу ничего не найдено"