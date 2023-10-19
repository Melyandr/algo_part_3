class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print(self.value),
        if self.right:
            self.right.PrintTree()


def invert_binary_tree(tree):
    if tree is None:
        return None
    temp = tree.left
    tree.left = tree.right
    tree.right = temp
    # Recursive call on subtrees
    invert_binary_tree(tree.left)
    invert_binary_tree(tree.right)
    return tree


root = BinaryTree(1)

root.left = BinaryTree(2)
root.right = BinaryTree(3)

root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)



change_tree = invert_binary_tree(root)
change_tree.PrintTree()




