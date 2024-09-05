
import pytest
import os
from generator_cpp import full_code_cpp
from generator_py import full_code_py
from problem_parser import check_all
from scraper import Problem




code_name_py = "./temp/main.py"
code_name_cpp = "./temp/main.cpp"
input_file = "./temp/input.txt"
EOFCheck = """try:\n\tinput()\n\traise Exception("File not fully read")\nexcept EOFError:\n\tpass"""


def write_file(file_name,code_str):
    with open(file_name,"w") as f:
        f.write(code_str)
    f.close()


def test_gen_pair_integers():
    #p = Problem("2008", "A")
    #inp = '''The only line of each test case contains two integers $a$ and $b$ ($0 \\le a, b \\le 10^9$)  — the number of '1's and the number of '2's in the array.'''
    #p = Problem("2008", "C")
    inp = '''The only line of each test case contains two integers $l$ and $r$ ($1 \\le l, r \\le 10^9$).

'''
    #code_str = full_code_cpp(check_all(p.input))
    code_str_py = full_code_py(check_all(inp))
    code_str_cpp = full_code_cpp(check_all(inp))
    #code_str = """T = int(input())\nfor i in range(T):\n\tx,y = map(int,input().split(' '))"""

    write_file(code_name_py, code_str_py)
    write_file(code_name_cpp, code_str_cpp)
    os.system("python3 ./temp/main.py < ./temp/input.txt ")
    os.system("g++ ./temp/main.cpp")
    os.system("./a.out < ./temp/input.txt")

