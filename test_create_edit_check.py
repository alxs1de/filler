from WebCompanyApi import WebCompanyApi
import requests
import pytest


api = "https://ru.yougile.com/api-v2/projects"

def create_company(name, users):
    company = {
        "name": name,
        "users": users
    }
    requests.post(api)

def test_add_new():
    name = "ГосУслуги"
    users = "4902b994-b806-4af4-acec-018ea5ea6468",
    "worker", "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018",
    "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    create_company(name, users)

def edit(name, users, deleted):
    company = {
        "name": name,
        "users": users,
        "deleted": deleted
    }
    requests.post(api)

def test_edit():
    name = "ГосУслуги"
    users = "4902b994-b806-4af4-acec-018ea5ea6468", "worker",
    "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018", 
    "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    deleted = "true"
    edit(name, users, deleted)
    requests.put(api+'4f6f0391-0f94-4d30-9b0e-99430a36d4fb')

def test_get_one_company():
    # Создаем компанию
    name = "ГосУслуги"
    users = "4902b994-b806-4af4-acec-018ea5ea6468", "worker",
    "8aeaeb9d-f94e-4c66-96d3-eb8d96fe7018", 
    "ee88efd5-5cb2-41a0-9ea2-295da25863d4"
    deleted = "true"
    result = api.create_company(name, users, deleted)
    new_id = result["id"]

    # Обращаемся к компании
    new_company = api.get_company(new_id)

    assert new_company["name"] == "title"
    assert new_company["users"] == "users"
    assert new_company["deleted"] is True
