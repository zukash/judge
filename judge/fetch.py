import requests
from pathlib import Path


def fetch(url):
    """ 問題文ページを保存する """

    # ~/.judge が無ければ作成
    p = Path.home() / ".judge"
    p.mkdir(exist_ok=True)

    # ~/.judge/problem_name を作成して保存
    problem_name = Path(url).name
    response = requests.get(url)
    with (p / problem_name).open(mode="w") as f:
        f.write(response.text)
