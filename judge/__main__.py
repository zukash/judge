from pathlib import Path

import fire

from .diff import diff
from .fetch import fetch
from .remove import remove


class Judge(object):
    def fetch(self, url):
        fetch(url)

    def diff(self):
        diff()

    def problems(self):
        problem_list = (Path.home() / ".judge").glob("*")
        print("\n".join([p.name for p in problem_list]))

    def rm(self):
        remove()


def main():
    fire.Fire(Judge)


if __name__ == "__main__":
    main()
