import unittest
from main import invert_binary_tree, BinaryTree

root2 = BinaryTree(1)

root2.left = BinaryTree(2)
root2.right = BinaryTree(3)

root2.left.left = BinaryTree(4)
root2.left.right = BinaryTree(5)

root2.right.left = BinaryTree(6)
root2.right.right = BinaryTree(7)


class MyTestCase(unittest.TestCase):

    def test_invert_no_odd(self):
        inver_tree = invert_binary_tree(root2)
        self.assertEqual(inver_tree.value, 1)
        self.assertEqual(inver_tree.left.value, 3)
        self.assertEqual(inver_tree.right.value, 2)
        self.assertEqual(inver_tree.left.left.value, 7)
        self.assertEqual(inver_tree.left.right.value, 6)
        self.assertEqual(inver_tree.right.left.value, 5)
        self.assertEqual(inver_tree.right.right.value, 4)


if __name__ == '__main__':
    unittest.main()
