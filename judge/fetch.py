import pickle
from pathlib import Path

import requests

from . import settings


def fetch(url):
    """ 問題文ページを保存する """

    # mkdir PROBLEM_DIR
    problem_dir = Path(settings.PROBLEM_DIR)
    problem_dir.mkdir(exist_ok=True)

    # load cookies
    cookies = {}
    try:
        with open(settings.COOKIES_FILE, "rb") as f:
            cookies = pickle.load(f)
    except Exception:
        pass

    # fetch a problem and save it
    problem_file = problem_dir / Path(url).name
    response = requests.get(url, cookies=cookies)
    problem_file.write_text(response.text)
