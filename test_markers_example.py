import pytest
import sys


def sum(a, b):
    return a + b

@pytest.mark.skip(reason="understood the cause - will fix later")
def test_sum():
    assert sum('1', 2) == 3
    
@pytest.mark.xfail(reason="expected to fail - will fix later")
def test_sum_xfail():
    assert sum('1', 2) == 4
    
@pytest.mark.skipif(sys.version_info > (3, 7), reason="functionality not supported for python 3.7 and above")
def test_sum_xfail_skipif():
    assert sum('1', 2) == 4
    
@pytest.mark.others
def test_sum():
    assert sum(1, 2) == 5
    
# pytest --markers    - to see all the builtin markers