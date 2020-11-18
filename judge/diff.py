import subprocess
import time
from difflib import Differ
from pathlib import Path

from pyfzf import FzfPrompt
from termcolor import cprint

from judge.parse import parse

from . import settings


def execute(command, sample_input):
    """ execute command and measure elapsed time """

    start_time = time.time()
    cp = subprocess.run(
        command,
        input=sample_input.encode(),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    elapsed_time = time.time() - start_time
    result, error = cp.stdout.decode(), cp.stderr.decode()

    return [result, error, elapsed_time]


def diff(quiet=False):
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
    solver_list = []
    for solver in Path().glob("**/*"):
        if solver.suffix.lstrip(".") in settings.SOLVER_EXTENSIONS:
            solver_list.append(solver)
    solver_selected = FzfPrompt().prompt(solver_list)[0]
    print(solver_selected)

    # create a command to excute the solver
    command = [Path(solver_selected).resolve()]
    if Path(solver_selected).suffix == ".py":
        command = ["python"] + command

    # check diff
    for sample_input, sample_output in zip(*parse(problem_selected)):
        # execute the solver
        result, error, elapsed_time = execute(command, sample_input)

        if error:
            print(error)
            exit()

        # difference between sample and result
        sample_output, result = sample_output.split("\n"), result.split("\n")
        diff = list(Differ().compare(sample_output, result))

        if len(diff) == len(sample_output):
            cprint("[AC]", "green", end=" ")
            cprint(f"{elapsed_time:.3f}", "grey")
            if not quiet:
                pass
        else:
            cprint("[WA]", "yellow", end=" ")
            cprint(f"{elapsed_time:.3f}", "grey")
            if not quiet:
                print("\n".join(diff))

        print("=================")
