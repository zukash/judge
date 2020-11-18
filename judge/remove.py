from pathlib import Path

from pyfzf import FzfPrompt

from . import settings


def remove():
    """ 問題を選択して削除する（複数選択可） """

    # choose problems
    problem_dir = Path(settings.PROBLEM_DIR)
    problem_list = [Path(p).name for p in problem_dir.glob("*")]
    assert len(problem_list) != 0
    problems_selected = FzfPrompt().prompt(problem_list, "--multi")

    # remove problems
    for problem_name in problems_selected:
        problem_file = problem_dir / problem_name
        problem_file.unlink()
        print(f"{problem_name} is successfully removed.")
