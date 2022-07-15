import pytest

def test_that_always_passes():
    a = 1
    b = 1
    assert a == b
    
    
def test_that_always_fails():
    a = 1
    b = 2
    assert a == b