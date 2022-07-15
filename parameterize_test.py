import pytest
 
call_par = ['4;4;True',
           '2;3;False',
           '5;5;True']
 
@pytest.mark.parametrize('call_par', call_par)
def test_math(call_par):
    """
    Our simple code will compare each scenario's first and second argument and check if they are equal. 
    We will print a message saying if they are equal or not.
    
    developer: kpc
    tester: kpc
    """
    (old_value, new_value, equals) = call_par.split(';')
    print("it is " + equals + " that " + old_value + " is equal to " + new_value)
    assert old_value == new_value
 
 
if __name__ == "__main__":
    pytest.main([__file__, "-k", "test_", "-v", "-s"])