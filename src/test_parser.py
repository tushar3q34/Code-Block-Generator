import pytest

from fetcher import fetch
from problem_parser import check_all
from scraper import Problem


def setup_testcases(p):
    for test in p.tests:
        test.input


def test_parser_int():
    inp, tests = fetch("2008_A")
    try:
        check_all(inp)
    except:
        pytest.fail("Parser failed for pair of integers")


# def test_parser_array():
#     inp, tests = fetch("2008_F")
#     try:
#         check_all(inp)
#     except:
#         pytest.fail("Parser failed for array of integers")


# def test_parser_string():
#     inp, tests = fetch("1922_A")
#     try:
#         check_all(inp)
#     except:
#         pytest.fail("Parser failed for string")


# def test_parser_matrix():
#     inp, tests = fetch("1980_E")
#     try:
#         check_all(inp)
#     except:
#         pytest.fail("Parser failed for matrix")

# def test_parser_string_array():
#     inp, tests = fetch("1980_E")
#     try:
#         check_all(inp)
#     except:
#         pytest.fail("Parser failed for array of strings")
