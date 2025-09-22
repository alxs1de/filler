import allure
import requests

@allure.title("Поиск фильмов по 2024 году")
@allure.description("Ввод названия фильма")
@allure.severity("critical")

def test_movies_451():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.1/films/search-by-keyword?keyword=451%20%D0%B3%D1%80%D0%B0%D0%B4%D1%83%D1%81%20%D0%BF%D0%BE%20%D1%84%D0%B0%D1%80%D0%B5%D0%BD%D0%B3%D0%B5%D0%B9%D1%82%D1%83&page=1",
                            headers=HEADERS)
    assert response.status_code == 200
    assert 'nameRu' in response.json()