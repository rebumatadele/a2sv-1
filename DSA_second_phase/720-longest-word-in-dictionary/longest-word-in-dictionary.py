class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]
        self.is_end = False
        self.count = 0

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def longestWord(self, words: List[str]) -> str:

        
        for val in words:
            current = self.root
            for v in val:
                temp = ord(v) - 97
                if not current.children[temp]:
                    current.children[temp] = TrieNode()

                current.count += 1
                current = current.children[temp]

            current.is_end = True

        words.sort(key = lambda x: (-len(x), x))

        for val in words:
            current = self.root
            flag = True
            for v in val:
                temp = ord(v) - ord("a")
                if not current.children[temp].is_end:
                    print("here")
                    flag = False
                    break
                current = current.children[temp]
            if flag and current.is_end:
                return val

        return ""
            