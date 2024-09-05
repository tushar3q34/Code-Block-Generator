
import pytest
import os
from generator_cpp import full_code_cpp
from generator_py import full_code_py
from problem_parser import check_all
from scraper import Problem
# from fetcher import fetch



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
    #inp = '''The only line of each test case contains two integers $l$ and $r$ ($1 \\le l, r \\le 10^9$).'''

    #p = Problem("2008", "D")
    #inp = '''The first line contains a single integer $t$ ($1 \\le t \\le 10^4$)  — the number of test cases.

#The first line of each test case contains a single integer $n$ ($1 \\le n \\le 2 \\cdot 10^5$)  — the number of elements in the array.

#The second line of each test case contains $n$ integers $p_1, p_2, ..., p_n$ ($1 \\le p_i \\le n$)  — the elements of the permutation.

#The third line of each test case contains a string $s$ of length $n$, consisting of '0' and '1'. If $s_i = 0$, then the number $p_i$ is colored black; if $s_i = 1%, then the number $p_i$ is colored white.

#It is guaranteed that the sum of $n$ across all test cases does not exceed %2 \\cdot 10^5$.'''

    #p = Problem("2002", "G")
    #inp = '''Each test contains multiple test cases. The first line contains the number of test cases $t$ ($1 \\le t \\le 100$). The description of the test cases follows.

#The first line of each test case contains a single integer $n$ ($2 \\le n \\le 20$) — the number of rows and columns.

#Each of the next $n - 1$ lines contains $n$ integers separated by single spaces — the matrix $d$ ($0 \\le d_{x, y} \\le 2n - 2$).

#Each of the next $n$ lines contains $n-1$ integers separated by single spaces — the matrix $r$ ($0 \\le r_{x, y} \\le 2n - 2$).

#It is guaranteed that the sum of all $n^3$ does not exceed $8000$.'''

    #p = Problem("2008", "G")
    inp = '''The first line contains a single integer $t$ ($1 \\le t \\le 10^4$)  — the number of test cases.

The first line of each test case contains two integers $n$ and $k$ ($1 \\le n \le 2 \\cdot 10^5, 1 \\le k \\le 10^9$)  — the number of elements in the array and the value $k$ for $mex_k$.

The second line of each test case contains $n$ integers $a_1, a_2, ..., a_n$ ($1 \\le a_i \\le 10^9$)  — the elements of the array.

It is guaranteed that the sum of $n$ across all test cases does not exceed %2 \\cdot 10^5$.

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