#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Unittest for max_integer([..])"""
    def test_ordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 6, 7]), 7)

    def test_unordered(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([1, 6, 3, 4, 2, 7, 5]), 7)

    def test_positives_and_negatives(self):
         """Unittest for max_integer([..])"""
         self.assertEqual(
            max_integer([-22, 580, 42, 30, -1024, -89, 2548, -5681, -25, -12,
                -5682, 264, 2354151, -665255485, -3210, 210, 521]), 2354151)

    def test_negatives(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([-25, -2, -450, -251, -1]), -1)

    def test_floats(self):
        """Unittest for max_integer([..])"""
        self.assertEqual(max_integer([0.2, 5.2, -8.3, -0.3, 9.2, -1.8]), 9.2)

    def test_integer(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(6)

    def test_one_float(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(3.14)

    def test_none(self):
        """Unittest for max_integer([..])"""
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()
