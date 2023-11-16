import unittest
from src.main import couples_for_wedding

graph1 = [[3], [1, 2], [2, 4], [3, 5]]
graph2 = [[5], [1, 2], [2, 4], [1, 3], [3, 5], [8, 10]]


class MyTestCase(unittest.TestCase):
    def test_graph1(self):
        self.assertEqual(couples_for_wedding(graph1), {"2/5", "4/3", "2/3", "4/5"})

    def test_graph2(self):
        self.assertEqual(
            couples_for_wedding(graph2), {"1/10", "5/10", "1/8", "3/8", "5/8", "3/10"}
        )


if __name__ == "__main__":
    unittest.main()
