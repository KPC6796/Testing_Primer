from logging import exception
import pytest

import pandas as pd
import numpy as np
import sys, math

###############################################################################
def tests_add():
    a = '4'
    b = '3'
    c = a + b
    if all(isinstance(i, int) for i in [a,b]):
        assert a + b == 7
    elif all(isinstance(i, str) for i in [a,b]):
        assert a + b == '43'
    else:
        print(exception)
        
###############################################################################        
    
@pytest.mark.skip    
def test_square():
    
    x = 5
    
    assert x**3 == 125
    assert x**1 == x
    assert x**2 == 10, "Result should be 25"
    
###############################################################################    
    
@pytest.mark.xfail
def test_double():
    
    x = 5

    assert x*2 == 12, "Result should be 10"
    
###############################################################################    
    
@pytest.mark.xfail(strict=True)  
def test_double_pass():
    
    x = 5

    assert x*2 == 10, "Result should be 10"
    
###############################################################################   

def is_perfect_square(n: int) -> bool:
    """Determine if any int i exists such that i × i = n."""
    s = math.sqrt(n)
    return s == int(s)

@pytest.mark.xfail(
    reason="Bug #1: Negative values not supported",
    strict=True
)
def test_negative():
    # When called with a negative value for n, this test raises ValueError!
    v = -4
    assert not is_perfect_square(w)
    
############################################################################### 

def is_perfect_square_corrected(n: int) -> bool:
    """Determine if any int i exists such that i × i = n."""
    if n < 0:
        return False  # No negative numbers are perfect squares

    s = math.sqrt(n)
    return s == int(s)

@pytest.mark.xfail(strict=True, raises=ValueError)
def test_negative_corrected():
    # When called with a negative value for n, this test raises ValueError!
    # See bug #1
    v = -4
    assert not is_perfect_square(w)

###############################################################################

@pytest.mark.skipif(sys.version_info<(3,9), "Functionality added after python version 3.9")
def merge_dict():    
    pycon = {2016: "Portland", 2018: "Cleveland"}
    europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}
    
    merged_dict = {}
    for key, value in europython.items():
        merged_dict[key] = value
    
    merged_dict_new = {**pycon, **europython}
    
    assert merged_dict == merged_dict_new
    
###############################################################################    
    
@pytest.mark.parametrize("input1, input2, output", [(2,2,4), (5,6,30), (8,9,80)])
def test_multiply(input1, input2, output):
    assert input1 * input2 == output
    
###############################################################################    
    
@pytest.fixture
def expected_data():
    a = 5
    b = 5
    return [a,b]

###############################################################################

def test_product(expected_data):
    output = 10
    assert expected_data[0] + expected_data[1] == output
    
###############################################################################    

def tokenize(lst):
    result = [sub.split() for sub in lst]
    return result

def test_tokenize():
    lst = ["I am learning pytest", "This is cool"]
    expected = [["I", "am", "learning", "pytest"], ["This", "is", "cool"]]
    
    result = tokenize(lst)
    
    assert result == expected
    
###############################################################################    
# @pytest.mark.skip(reason="Fetching data from external source i.e., conftest.py")
def test_if_important(important_value):
    assert important_value == True

###############################################################################
    
        
if __name__=='__main__':
    pass


    """Commands:
    python -m pytest tests\demo_test.py  # Run all tests in demo_test.py
    pytest demo_test.py
    pytest -v -s demo_test.py (v for verbosity, s to print output to console)
    pytest -n 3 -v demo_test.py (3 worker nodes - sending tests to multiple cpus and executing test cases in parallel)
    pytest demo_test.py --html=report.html (to export the report in html format)
    pytest -v demo_test.py::test_tokenize
    """