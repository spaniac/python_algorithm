import requests


def request_all_users():
    return request_get_user_list()


def request_get_user_list():
    response = requests.get("http://127.0.0.1:8000/blog")
    return response.json()
