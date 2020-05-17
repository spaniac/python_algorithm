import requests


def request_get_user_list():
    response = requests.get("http://127.0.0.1:8000/blog")
    return response.json()
