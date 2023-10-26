
def square_integers(int_list):
    return [i ** 2 for i in int_list]

# Unit test for test_square_integers()


import pytest
def test_square_integers():
    '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
    assert(square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25])
    assert(square_integers([-1, -2, -3, -4, -5]) == [1, 4, 9, 16, 25])
