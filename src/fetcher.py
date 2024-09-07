import os

from scraper import Problem

path = os.path.dirname(os.path.realpath(__file__))
path = f"{path}/problems"


def write_file(file_name, code_str):
    with open(file_name, "w") as f:
        f.write(code_str)


def fetch(prob):
    if isinstance(prob, str):
        contestId, index = prob.split("_")
    else:
        contestId, index = prob

    try:
        p = Problem(contestId, index)
        p = {"input": rf"{p.input}", "tests": rf"{p.tests}"}
        write_file(f"{path}/{contestId}_{index}.txt", str(p))
    except:
        with open(f"{path}/{contestId}_{index}.txt", "r") as f:
            p = eval(f.read())

    return p["input"], p["tests"]
