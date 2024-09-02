from scraper import *
import pytest
from problem_parser import *

def test_scraper():
    p = Problem("1980","G")
    try:
        p.input
    except:
        pytest.fail("Scraper could not fetch")
        

def test_parser_int():
    p = Problem("2008","A")
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

def test_parser_string(p.input):
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