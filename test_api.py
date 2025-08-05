from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pytest
import allure
import requests

token = '20eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTQ1OTQ5MzgsImlhdCI6MTc1NDQyNjkzOCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImQ5OWYzMzliZWMzYmU4NzNmYzE2NDhjYTNkZjhiODIzM2E5NjVlNjA4MDQ1ZTc2OTRlYjU5MDZjOWQ5ZTVmNTQiLCJ0eXBlIjoxMH0.koKtfCCldwSXW6uhdzu6nOqL2Y5JadqGCtnaRDHh0k8'
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

def test_put():

    url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=Solo%20Leveling&abTestGroup=1'
    body = {"title": "ГосУслуги"}
    response = requests.put(url, headers=headers, json=body)

    assert response.status_code == 200

def test_get_empty():

    url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=Solo%20Leveling&abTestGroup=1'
    body = {"title": ""}
    response = requests.get(url, headers=headers, json=body)

    assert response.status_code == 200


def test_get_cirillic():

    url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=Solo%20Leveling&abTestGroup=1'
    body = {"title": "привет"}
    response = requests.get(url, headers=headers, json=body)

    assert response.status_code == 200

def test_get_latin():

    url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=Solo%20Leveling&abTestGroup=1'
    body = {"title": "hi"}
    response = requests.get(url, headers=headers, json=body)

    assert response.status_code == 200

def test_get_hieroglyphs():

    url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=Solo%20Leveling&abTestGroup=1'
    body = {"title": "أهلاً"}
    response = requests.get(url, headers=headers, json=body)

    assert response.status_code == 200