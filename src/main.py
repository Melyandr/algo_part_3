class Node:
    def __init__(self):
        self.children = {}
        self.end_of_word = False


class PrefixTrie:
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


def fill_words_to_trie(patterns) -> PrefixTrie:
    obj = PrefixTrie()
    for i in patterns:
        obj.insert(i)
    return obj


if __name__ == "__main__":
    patterns = ["do", "dos", "dog", "mul"]
    obj_with_patterns = fill_words_to_trie(patterns)


