#!/usr/bin/env python3

from generated.task2 import square_integers

class TestSquareIntegers:
    '''square_integers()'''

    def test_square_integers(self):
        '''returns squared ints for [1, 2, 3, 4, 5] and [-1, -2, -3, -4, -5]'''
        assert(square_integers([1, 2, 3, 4, 5]) == [1, 4, 9, 16, 25])
        assert(square_integers([-1, -2, -3, -4, -5]) == [1, 4, 9, 16, 25])