import requests


class CompanyApi:

    def __init__(self, url) -> None:
        self.url = url
    # Добавить компанию:


    def create_company(self, title, user1, user2, user1_class, user2_class=""):
        company = {
            "name": title,
            "user_1": user1,
            "user_2": user2,
            "user_1_class": user1_class,
            "user_2_class": user2_class
        }
        resp = requests.post(self.url,
                             json=company)
        return resp.json()



    def edit_company(self, new_id, new_name, new_descr):
    # Получаем токен
        client_token = self.get_token()

    # Формируем URL с параметром client_token
        url_with_token = f"{self.url}/company/update/{new_id}?client_token={client_token}"

    # Вызываем словарь и кладем в него описание компании
        company = {
            "name": new_name,  # Новое имя компании
            "description": new_descr  # Новое описание компании
        }

    # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.patch(url_with_token, json=company)

    # Результат вернется в JSON, мы его прокинем в тест
        return resp.json()
    


    def get_company(self, id):
        resp = requests.get(self.url + '4f6f0391-0f94-4d30-9b0e-99430a36d4fb' + str(id))
        return resp.json()