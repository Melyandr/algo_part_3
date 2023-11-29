class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class PrefixTree:
    def __init__(self):
        self.root = Node()

    def insert(self, word: str):
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                pointer.children[letter] = Node()
            pointer = pointer.children[letter]
        pointer.end_of_word = True

    def search(self, word: str) -> bool:
        pointer = self.root
        for letter in word:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]

        if pointer.end_of_word:
            return True
        else:
            return False

    def starts_with(self, prefix: str) -> bool:
        pointer = self.root
        for letter in prefix:
            if letter not in pointer.children:
                return False
            pointer = pointer.children[letter]
        return True


def fill_words_to_trie(patterns) -> PrefixTree:
    obj = PrefixTree()
    for i in patterns:
        obj.insert(i)
    return obj


if __name__ == "__main__":
    # obj = PrefixTree()
    # obj.insert("dog")
    # obj.insert("dos")
    # obj.insert("do")
    # obj.insert("mul")
    # print(obj.starts_with("do"))
    # print(obj.search("dos"))
    patterns = ["do", "dos", "dog", "mul"]
    obj_with_patterns = fill_words_to_trie(patterns)
    print(obj_with_patterns.search("mul"))
    print(obj_with_patterns.starts_with("p"))

    # print(obj_with_patterns)
