import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_ordinary(self):
        self.assertEqual(binary_search([30, 11, 23, 4, 20], 5), 30)

    def test_the_same_piles(self):
        self.assertEqual(binary_search([7, 7, 7, 7, 7, 7, 7], 7), 7)

    def test_list_bounds(self):
        with self.assertRaises(ValueError):
            binary_search([-3, 6, 7, 11], 8)

    def test_time_bounds(self):
        with self.assertRaises(ValueError):
            binary_search([3, 6, 7, 11], 2)

    def test_pile_bounds(self):
        with self.assertRaises(ValueError):
            binary_search([0.5, 6, 7, 11], 4)


if __name__ == '__main__':
    unittest.main()
