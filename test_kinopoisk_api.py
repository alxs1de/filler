import allure
import requests

@allure.title("Поиск фильмов по 2024 году")
@allure.description("Ввод названия фильма")
@allure.severity("critical")
# def test_movies_2024():
#     HEADERS = {
#         "accept": "application/json",
#         "X-API-KEY": ""
#     }
#     response = requests.get("https://api.kinopoisk.dev/v1.4/movie?page=1&limit=10&type=movie&year=2024",
#                             headers=HEADERS)
#     assert response.status_code == 200

def test_movies_2024():
    HEADERS = {
        "accept": "application/json",
        "X-API-KEY": "354712b4-eeb2-4295-8f7a-161d72468a8f"
    }
    response = requests.get("https://kinopoiskapiunofficial.tech/api/v2.2/films?order=RATING&type=ALL&ratingFrom=0&ratingTo=10&yearFrom=2024&yearTo=2024&page=1",
                            headers=HEADERS)
    assert response.status_code == 200