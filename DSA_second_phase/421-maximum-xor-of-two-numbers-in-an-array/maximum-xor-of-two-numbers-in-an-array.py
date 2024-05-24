class TrieNode:
    def __init__(self):
        self.children = [None, None]

    def addWord(self, word):
        current = self
        for b in range(32, -1, -1):
            curr = 1 if word & (1<<b) else 0
            
            if not current.children[curr]:
                current.children[curr] = TrieNode()
            current = current.children[curr]

class Solution:
    def __init__(self):
        self.root = TrieNode()
    def findMaximumXOR(self, nums: List[int]) -> int:

        current = self.root
        for num in nums:
            current.addWord(num)

        g_max = 0
        for bit in nums:
            current = self.root
            ans = 0
            for b in range(32, -1, -1):
                curr = 1 if bit & (1<<b) else 0

                if current.children[curr ^ 1]:
                    current = current.children[curr ^ 1]
                    ans |= 1 << b
                else:
                    current = current.children[curr]

            g_max = max(g_max, ans)
        return g_max



