from pathlib import Path

from pyfzf import FzfPrompt


def remove():
    """ 問題を選択して削除する（複数選択可） """

    # choose problems
    problem_dir = Path.home() / ".judge"
    problem_list = [Path(p).name for p in problem_dir.glob("*")]
    assert len(problem_list) != 0
    problems_selected = FzfPrompt().prompt(problem_list, "--multi")
    print(problems_selected)

    # remove problems
    for problem_name in problems_selected:
        problem_file = Path.home() / ".judge" / problem_name
        problem_file.unlink()
        print(f"{problem_name} is successfully removed.")
