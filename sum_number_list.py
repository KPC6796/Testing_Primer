def sum_number_list(list_numbers):
    """Loop over list with numbers and returns the sum of numbers.
 
    Args:
        list_numbers (list): List with numbers.
 
    Returns:
        float: Sum of numbers in list_numbers
 
    """
    total_sum = 0.0
    for n in list_numbers:
        total_sum += n
 
    return total_sum