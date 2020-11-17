import pickle
from pathlib import Path

import requests

from . import settings


def fetch(url):
    """ 問題文ページを保存する """

    # ~/.judge が無ければ作成
    p = Path.home() / ".judge"
    p.mkdir(exist_ok=True)

    # load cookies
    cookies = {}
    try:
        with open(settings.COOKIES_FILE, "rb") as f:
            cookies = pickle.load(f)
    except Exception:
        pass

    # ~/.judge/problem_name を作成して保存
    problem_name = Path(url).name
    response = requests.get(url, cookies=cookies)
    with (p / problem_name).open(mode="w") as f:
        f.write(response.text)
