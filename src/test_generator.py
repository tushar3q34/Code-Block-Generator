
import pytest
import os
from generator_cpp import full_code_cpp
from problem_parser import check_all
from scraper import Problem
# from fetcher import fetch



code_name = "src/temp/main.py"
input_file = "src/temp/input.txt"
EOFCheck = """try:\n\tinput()\n\traise Exception("File not fully read")\nexcept EOFError:\n\tpass"""


def write_file(file_name,code_str):
    with open(file_name,"w") as f:
        f.write(code_str)
    f.close()


def test_gen_pair_integers():
    p = Problem("2008", "A")
    #code_str = full_code_cpp(check_all(p.input))
    code_str = """T = int(input())\nfor i in range(T):\n\tx,y = map(int,input().split(' '))"""

    write_file(code_name,code_str)
    for test in p.tests:
        test_raw = test.input[6:] # dropping the input word
        write_file(input_file,test_raw)
        os.system("python3 main.py < input.txt ")

def test_gen_pair_integers():
    prob = "2008A"
    input_string,tests = fetch(prob)
    #code_str = full_code_cpp(check_all(input_string))
    code_str = """T = int(input())\nfor i in range(T):\n\tx,y = map(int,input().split(' '))"""

    write_file(code_name,code_str)
    for test in tests:
        test_raw = test[6:] # dropping the input word
        write_file(input_file,test_raw)
        os.system("python3 main.py < input.txt ")

test_gen_pair_integers()