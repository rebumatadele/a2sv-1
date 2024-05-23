class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root
        for val in word:
            ind = ord(val) - 97
            if not current.children[ind]:
                current.children[ind] = TrieNode()
            current = current.children[ind]
        current.is_end = True   

    def search(self, word: str) -> bool:
        current = self.root
        for val in word:
            ind = ord(val) - 97
            if not current.children[ind]:
                return False
            current = current.children[ind]
        if current.is_end:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for val in prefix:
            ind = ord(val) - 97
            if not current.children[ind]:
                return False
            current = current.children[ind]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)