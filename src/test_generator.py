import os

from fetcher import fetch
from generator_cpp import full_code_cpp
from generator_py import full_code_py
from problem_parser import check_all

dir = os.path.dirname(os.path.realpath(__file__))

code_name_py = f"{dir}/tmp/main.py"
code_name_cpp = f"{dir}/tmp/main.cpp"
input_file = f"{dir}/tmp/input.txt"
EOFCheck = """try:\n\tinput()\n\traise Exception("File not fully read")\nexcept EOFError:\n\tpass"""


def write_file(file_name, code_str):
    with open(file_name, "w") as f:
        f.write(code_str)
    f.close()


def test_gen_pair_integers():
    inp, tests = fetch("2008_G")

    code_str_py = full_code_py(check_all(inp))
    code_str_cpp = full_code_cpp(check_all(inp))

    write_file(code_name_py, code_str_py)
    write_file(code_name_cpp, code_str_cpp)

    os.system(f"python3 {code_name_py} < {input_file} ")

    os.system(f"g++ -o ./a.out {code_name_cpp}")
    os.system(f"./a.out < {input_file}")
