import unittest
from src.main import find_derived_word, find_max_length


class TestFindDerivedWord(unittest.TestCase):
    def test_find_derived_word(self):
        list_with_words = ["b", "bcad", "bca", "bad", "bd"]
        expected_output = [[], [1, 1, 1, 1], [], [1], [1]]
        result = find_derived_word(list_with_words)
        self.assertEqual(result, expected_output)

    def test_find_max_length(self):
        input_list = [[], [1, 1, 1, 1], [], [1], [1]]
        max_length = find_max_length(input_list)
        self.assertEqual(max_length, 4)


if __name__ == "__main__":
    unittest.main()
