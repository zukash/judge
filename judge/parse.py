import re
from pathlib import Path

from bs4 import BeautifulSoup

from . import settings


def parse(problem_name):
    """ 問題文からテストケースを抜き出して返す """

    problem_file = Path(settings.PROBLEM_DIR) / problem_name
    if not problem_file.exists():
        print("Error: " + problem_name + " doesn't exist.")
        exit()

    soup = BeautifulSoup(problem_file.read_text(), "html.parser")
    inputs = soup.find_all("h3", text=re.compile("入力例"))
    inputs = [si.find_parent().find("pre").text.lstrip() for si in inputs]
    outputs = soup.find_all("h3", text=re.compile("出力例"))
    outputs = [so.find_parent().find("pre").text.lstrip() for so in outputs]

    return [inputs, outputs]
