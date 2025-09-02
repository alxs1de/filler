import requests

token = ' eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3NTcwMDkzNTksImlhdCI6MTc1Njg0MTM1OSwiaXNzIjoiL2FwaS92MS9hdXRoL2Fub255bW91cyIsInN1YiI6ImFmYmM0MTQ1ODNiNDM5NjE2ZDY1MDIzMjJiNGExZDlhZjA1MDJkMGFmNjkzZjI5MTIzZGRjNjFlODMyYjY3ZmEiLCJ0eXBlIjoxMH0.tIgj03TMdV79rJoONeubz1RYHhapyAScqhLlkzWSNM4'
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
#     assert 'content' in response.json()

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

### ДРУГИЕ ТЕСТЫ

def test_hello():
    url = 'https://web-agr.chitai-gorod.ru/web/api/v2/search/facet-search?customerCityId=213&phrase=451%C2%B0%20%D0%BF%D0%BE%20%D0%A4%D0%B0%D1%80%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D1%82%D1%83&abTestGroup=1'
    response = requests.get(url, headers=headers)

    assert response.status_code == 200
    print(response.json())
    assert 'content' in response.json()
