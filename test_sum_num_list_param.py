import pytest
 
from sum_number_list import sum_number_list
 
 
@pytest.mark.parametrize("list_numbers, result", [
    # test 1
    ([1, 2, 3, 3], 9),
 
    # test 2
    ([1], 1),
 
    # test 3
    ([1, 2], 3),
 
    # test 4
    ([1, 3], 4),
 
    # test 5
    ([2], 2)
])
def test_sum_number_list_using_parametrize(list_numbers, result):
    assert sum_number_list(list_numbers) == result
    
    
# pytest -vv