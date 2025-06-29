import requests

class WebCompanyApi:

    def __init__(self, url) -> None:
        self.url = url
    # Добавить компанию:


    def create_company(self, name, users=""):
        company = {
            "name": name,
            "users": users
        }
        resp = requests.post(self.url,
                             json=company)
        return resp.json()


    def edit_company(self, new_id, new_name, new_users):
    # Получаем токен
        client_token = self.get_token()
        url_with_token = f"{self.url}/company/update/{new_id}?client_token={client_token}"

    # Вызываем словарь и кладем в него описание компании
        company = {
            "name": new_name,
            "users": new_users
        }

    # Метод отправляет запрос по URL, передает заголовки и тело
        resp = requests.put(url_with_token, json=company)

    # Результат вернется в JSON, мы его прокинем в тест
        return resp.json()
    


    def get_company(self, id):
        resp = requests.get(self.url+ str(id))
        return resp.json()