import pickle
import re
from getpass import getpass

import requests

from . import settings


def login(username):
    """ login and fetch the REVEL_SESSION """

    password = getpass("Password: ")

    url = "https://atcoder.jp/login"
    res = requests.get(url)
    csrf_token = re.findall(r'csrfToken = "(.+)"', res.text)[0]
    payload = {
        "username": username,
        "password": password,
        "csrf_token": csrf_token,
    }
    res = requests.post(url, payload, cookies=res.cookies)

    error_message = "Username or Password is incorrect."
    if error_message in res.text:
        print(error_message)
        exit()

    with open(settings.COOKIES_FILE, "wb") as f:
        pickle.dump(res.cookies, f)

    print("successfully logged in.")
