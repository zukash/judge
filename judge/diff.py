import subprocess
from difflib import Differ
from pathlib import Path

from pyfzf import FzfPrompt

from judge.parse import parse


def diff():
    """ テストケースとの差を返す """

    # choose the problem
    print("problem: ", end="")
    problem_dir = Path.home() / ".judge"
    problem_list = [Path(p).name for p in problem_dir.glob("*")]
    assert len(problem_list) != 0
    problem_selected = FzfPrompt().prompt(problem_list)[0]
    print(problem_selected)

    # choose the solver
    print("solver: ", end="")
    solver_list = Path().glob("*")
    solver_selected = FzfPrompt().prompt(solver_list)[0]
    print(solver_selected)

    # create a command to excute the solver
    command = [Path(solver_selected).resolve()]
    if Path(solver_selected).suffix == ".py":
        command = ["python"] + command

    # check diff
    for sample_input, sample_output in zip(*parse(problem_selected)):
        # execute the solver
        cp = subprocess.run(
            command,
            input=sample_input.encode(),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )
        result, error = cp.stdout.decode(), cp.stderr.decode()

        if error:
            print(error)
            exit()

        # difference between sample and result
        sample_output, result = sample_output.split("\n"), result.split("\n")
        diff = list(Differ().compare(sample_output, result))

        if len(diff) == len(sample_output):
            print("[AC]")
        else:
            print("[WA]")
            print("\n".join(diff))

        print("=================")
