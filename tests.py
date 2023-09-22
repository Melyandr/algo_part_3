import unittest
from main import *


class QuickSortTest(unittest.TestCase):
    def test_odd_list(self):
        self.assertEqual(quick_sort([19, 2, 45, 10, 6, 11, 121, 5, 33, 27, 13], 3),
                         "The number is  33, The index is  8")

    def test_pair_list(self):
        self.assertEqual(quick_sort([19, 2, 45, 10, 6, 11, 121, 5, 33, 27], 5), "The number is  19, The index is  5")

    def test_k_is_over(self):
        self.assertEqual(quick_sort([19, 2, 45, 10, 6, 11, 121, 5, 33, 27, 13], 13),
                         "k is greater than the length of the list")

    def test_find_first_element(self):
        self.assertEqual(quick_sort([19], 1),
                         (19, 0))

    def test_empty_list(self):
        self.assertEqual(quick_sort([], 1), "your list is empty")


if __name__ == '__main__':
    unittest.main()
