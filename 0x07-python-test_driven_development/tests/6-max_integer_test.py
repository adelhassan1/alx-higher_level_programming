#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):

    def test_import(self):
        self.assertTrue(__import__('6-max_integer').max_integer)

    def test_integer(self):
        """Test if it gives must integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 5, 6, 3, 9, 2]), 9)
        self.assertEqual(max_integer([-1, -2, -4, -5, -9]), -1)
        self.assertEqual(max_integer([-1, 4, -9]), 4)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer({0: 'a', 1: 'z', 2: 'c'}), 'z')

    def test_types(self):
        """Make sure type errors are raised"""
        self.assertRaises(TypeError, max_integer, [1, 2, "School"])
        self.assertRaises(TypeError, max_integer, [1, 2, (1, 2)])
        self.assertRaises(TypeError, max_integer, [1, 2, [1, 5]])
        self.assertRaises(TypeError, max_integer, [1, 2, 5+3j])
        self.assertRaises(TypeError, max_integer, None)
        self.assertRaises(TypeError, max_integer, True)
        self.assertRaises(TypeError, max_integer, -3)
        self.assertRaises(KeyError, max_integer, {'a': 2, 'b':1, 'c':3})

if __name__ == '__main__':
    unittest.main()
