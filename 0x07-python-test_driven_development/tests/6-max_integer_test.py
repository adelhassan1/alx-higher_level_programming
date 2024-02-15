#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Tests for max integer"""

    def test_integer(self):
        """Test if it gives must integer"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([3, 5, 6, 3, 9, 2]), 9)
        self.assertEqual(max_integer([-1, -2, -4, -5, -9]), -1)
        self.assertEqual(max_integer([-1, 4, -9]), 4)

    def test_types(self):
        """Make sure type errors are raised"""
        self.assertRaises(TypeError, max_integer, [1, 2, "School"])
        self.assertRaises(TypeError, max_integer, [1, 2, (1, 2)])
        self.assertRaises(TypeError, max_integer, [1, 2, [1, 5]])
        self.assertRaises(TypeError, max_integer, [1, 2, 5+3j])
        self.assertRaises(TypeError, max_integer, None)
