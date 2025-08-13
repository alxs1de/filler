from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pytest
import allure
import requests

token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTUyNTIxOTgsImlhdCI6MTc1NTA4NDE5OCwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6IjhiNDk3NGI3ODdjNzgxMGZmMjc0MzU4ZDFmZTY3Nzk4ZjIxNGIwNjQ5ZWNlZDc5MzU1YTI0YWRlNjM0MTBkN2IiLCJ0eXBlIjoxMH0.aD74B81UCJPg9mp_H5153HLpyWrtBBz7E5XyJ0_3-4M'
headers = {
    "Authorization": f"Bearer {token}",
    "Content-Type": "application/json"
}

# def test_get_numbers_degrees():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=451%C2%B0%20%D0%BF%D0%BE%20%D0%A4%D0%B0%D1%80%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D1%82%D1%83&abTestGroup=1'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 200

# def test_get_empty():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=&abTestGroup=1'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 403
#
#
# def test_get_cirillic():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=%D0%9F%D1%80%D0%B5%D1%81%D1%82%D1%83%D0%BF%D0%BB%D0%B5%D0%BD%D0%B8%D0%B5%20%D0%B8%20%D0%9D%D0%B0%D0%BA%D0%B0%D0%B7%D0%B0%D0%BD%D0%B8%D0%B5&abTestGroup=1'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 200
#
# def test_get_latin():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=War%20and%20Peace&abTestGroup=1'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 200
#
# def test_get_hieroglyphs():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=%E0%A4%B0%E0%A4%95%E0%A5%8D%E0%A4%A4%20%E0%A4%AE%E0%A5%87%E0%A4%B0%E0%A4%BF%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%A8&abTestGroup=1'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 200

### ДРУГИЕ ТЕСТЫ (МЕТОДЫ PRODUCT И SEMANTIC)


# def test_big_test():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/product?customerCityId=213&products%5Bpage%5D=1&products%5Bper-page%5D=60&phrase=good%20morning&abTestGroup=1'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 200
#
# def test_bigger_test():
#
#     url = 'https://web-agr.chitai-gorod.ru/web/api/v1/recommend/semantic?phrase=good+morning&perPage=48'
#     response = requests.get(url, headers=headers)
#
#     assert response.status_code == 200