import re
from pathlib import Path

from bs4 import BeautifulSoup


def parse(problem_name):
    """ 問題文からテストケースを抜き出して返す """

    problem_file = Path.home() / ".judge" / problem_name
    if not problem_file.exists():
        print("Error: " + problem_name + " doesn't exist.")
        exit()

    soup = BeautifulSoup(problem_file.read_text(), "html.parser")
    inputs = soup.find_all("h3", text=re.compile("入力例"))
    inputs = [si.find_parent().find("pre").text for si in inputs]
    outputs = soup.find_all("h3", text=re.compile("出力例"))
    outputs = [so.find_parent().find("pre").text for so in outputs]

    return [inputs, outputs]
