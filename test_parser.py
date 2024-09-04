import pytest

# from generator import generate
from problem_parser import check_all
from scraper import Problem


def setup_testcases(p):
    # generate(check_all(p.input))
    for test in p.tests:
        test.input


def test_scraper():
    try:
        p = Problem("1980", "G")
        assert len(p.input) == 12
    except:
        pytest.fail("Scraper could not fetch")


def test_parser_int():
    p = Problem("2008", "A")
    try:
        check_all(p.input)
    except:
        pytest.fail("Parser failed for pair of integers")


# def test_parser_array():
#     p = Problem("2008", "F")
#     try:
#         check_all(p.input)
#     except:
#         pytest.fail("Parser failed for array of integers")


def test_parser_string():
    p = Problem("1922", "A")
    try:
        check_all(p.input)
    except:
        pytest.fail("Parser failed for string")


# def test_parser_matrix():
#     p = Problem("1980", "E")
#     try:
#         check_all(p.input)
#     except:
#         pytest.fail("Parser failed for matrix")

# def test_parser_string_array():
#     p = Problem("1980", "E")
#     try:
#         check_all(p.input)
#     except:
#         pytest.fail("Parser failed for array of strings")
