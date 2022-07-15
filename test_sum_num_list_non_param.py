import pytest
 
from sum_number_list import sum_number_list
 
 
def test_sum_number_list_using_non_parametrize():
    # test 1
    assert sum_number_list([1, 2, 3, 3]) == 9
 
    # test 2
    assert sum_number_list([1]) == 1
 
    # test 3
    assert sum_number_list([1, 2]) == 3
 
    # test 4
    assert sum_number_list([1, 3]) == 4
 
    # test 5
    assert sum_number_list([2]) == 2