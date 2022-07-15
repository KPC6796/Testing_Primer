import pytest

def validate_input(input_data):
    if input_data == "":
        raise ValueError("Input cannot be empty")
    return input_data


def test_validate_input_1():
    with pytest.raises(ValueError):
        validate_input("")
    assert validate_input("test") == "text"
    
def test_validate_input_2():
    with pytest.raises(ValueError, match="Input cannot be empty"):
        validate_input("test")