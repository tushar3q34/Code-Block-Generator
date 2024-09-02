from scraper import *
import pytest
from problem_parser import *


def test_scraper():
    p = Problem("1980","G")
    try:
        p.input
        
    except:
        pytest.fail("Scraper could not fetch")
        

# def test_parser_int():
#     p = Problem("2008","A")
#     try:
#         check_all()
#     except:
#         pytest.fail("Parser failed for pair of integers")
