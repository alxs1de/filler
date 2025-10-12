import allure
import requests

@allure.title("Поиск фильмов по названию 'Мстители'")
@allure.description("Ввод названия фильма")
@allure.severity("critical")

def test_movies_451():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword=%D0%9C%D1%81%D1%82%D0%B8%D1%82%D0%B5%D0%BB%D0%B8&page=1",
                            headers=HEADERS)
    assert response.status_code == 200
    assert response.json()['films'][0].get('nameRu') == 'Мстители'
