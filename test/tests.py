import unittest

from src.main import findAllMotherVertices


V = 8
adj = [[] for _ in range(V)]

adj[0].append(1)
adj[1].append(2)
adj[1].append(4)
adj[1].append(5)
adj[2].append(3)
adj[2].append(6)
adj[3].append(2)
adj[3].append(7)
adj[4].append(0)
adj[4].append(5)
adj[5].append(6)
adj[6].append(5)
adj[6].append(7)


class MyTestCase(unittest.TestCase):
    def test_FindVertices(self):
        self.assertEqual(findAllMotherVertices(adj), 0)


if __name__ == "__main__":
    unittest.main()
