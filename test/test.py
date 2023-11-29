import unittest
from src.main import PrefixTree


class TestPrefixTree(unittest.TestCase):
    def setUp(self):
        self.obj = PrefixTree()
        self.obj.insert("dog")
        self.obj.insert("dos")
        self.obj.insert("do")
        self.obj.insert("mul")

    def test_search(self):
        self.assertEqual(self.obj.search("dos"), True)

    def test_start_with(self):
        self.assertEqual(self.obj.starts_with("d"), True)


if __name__ == "__main__":
    unittest.main()
