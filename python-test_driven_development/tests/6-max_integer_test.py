#!/usr/bin/python3
"""max integer test"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class Maxtest(unittest.TestCase):
    """Testing"""
    def testing_max_at_end(self):
        """Testing at end"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def testing_max_at_beginning(self):
        """"Testing at beginning"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def testing_max_at_middle(self):
        """Testing at middle"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def testing_with_one_int(self):
        """Testing with one element"""
        self.assertEqual(max_integer([1]), 1)

    def testing_with_the_same_int(self):
        """Testing with the same int"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
    
    def testing_with_none(self):
        """Testing with nothing"""
        self.assertEqual(max_integer([]), None)
    
    def testing_with_negative(self):
        """Testing with negatives"""
        self.assertEqual(max_integer([-1, -4, -3, -2]), -4)
