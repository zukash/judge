from pathlib import Path

import fire

from . import settings
from .config import config
from .diff import diff
from .fetch import fetch
from .login import login
from .remove import remove


class Judge(object):
    def fetch(self, url):
        fetch(url)

    def diff(self, quiet=False):
        diff(quiet)

    def problems(self):
        problem_list = Path(settings.PROBLEM_DIR).glob("*")
        print("\n".join([p.name for p in problem_list]))

    def rm(self):
        remove()

    def login(self, username):
        login(username)

    def config(self, name, value):
        config(name, value)


def main():
    fire.Fire(Judge)


if __name__ == "__main__":
    main()
