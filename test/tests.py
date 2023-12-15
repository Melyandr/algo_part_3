import unittest
from src.main import max_length


class TestFindDerivedWord(unittest.TestCase):

    def test_find_derived_word(self):
        list_with_words = ["b", "bcad", "bca", "bad", "bd"]
        expected_output =4
        result = max_length(list_with_words)
        self.assertEqual(result, expected_output)



if __name__ == '__main__':
    unittest.main()
