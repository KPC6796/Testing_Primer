import pytest


@pytest.fixture(scope="module")
def set_up():
    print("Runs once before every test of set_up")
    yield
    print("Runs once after every test at the end of set_up")
    
@pytest.fixture(scope="function")
def tear_down():
    print("Runs once before every test of tear_down")
    yield
    print("Runs once after every test at the end of tear_down")
    
def test_methodA(set_up):
    print("Runs once before every test")
    print("Runs once after every test")
    
def test_methodB(tear_down):
    print("Runs once before every test")
    print("Runs once after every test")
    
@pytest.mark.others
def test_methodC():
    print("Runs once before every test")
    print("Runs once after every test")