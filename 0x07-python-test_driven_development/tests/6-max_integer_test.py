#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMatrixInteger(unittest.TestCase):
    """Suite test for max_integer function"""
    def test_max_integer(self):
        self.assertEqual(max_integer([5, -1, 180]), 180)

    def test_empty_list(self):
        self.assertEqual(max_integer([]), None)

    def test_repeated_number(self):
        self.assertEqual(max_integer([1000, 1000, 1000]), 1000)

    def test_float_numbers(self):
        self.assertEqual(max_integer([0, 51, 12, 49]), 51)

    def test_max_operated_integer(self):
        self.assertEqual(max_integer([-3, -6 * -6, 12, -1]), 36)

    def test_neg_numbers(self):
        self.assertEqual(max_integer([-100, -6, -20, -1]), -1)

    def test_max_at_beginning(self):
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)

    def test_zero_number(self):
        self.assertEqual(max_integer([0, 0]), 0)

    def test_big_list(self):
        self.assertEqual(max_integer([i for i in range(900, 1001)]), 1000)

    def test_list_with_loop(self):
        my_list = [1, 2, 3, 4, 5]
        self.assertEqual(max_integer([i * 5 for i in my_list]), 25)

    def test_one_number_in_a_list(self):
        self.assertEqual(max_integer([1]), 1)

    def test_string_number_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([0, '1'])

    def test_tuple_in_a_list(self):
        with self.assertRaises(TypeError):
            max_integer([10, (45, 0)])

    def test_dictionary(self):
        with self.assertRaises(KeyError):
            max_integer({'key1': 45, 'key2': 98})

    def test_number(self):
        with self.assertRaises(TypeError):
            max_integer(34)
