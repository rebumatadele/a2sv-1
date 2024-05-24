class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False
        self.count = 0
    def addWord(self, word):
        current = self
        current.count += 1
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
            current.count += 1
        current.is_word = True
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        root = TrieNode()
        for word in wordDict:
            root.addWord(word)

        n = len(s) + 1
        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            current = root
            for j in range(i, n):
                if s[j-1] in current.children:
                    current = current.children[s[j-1]]
                    if current.is_word:
                        dp[j] = dp[j] or dp[i-1]
                else:
                    break
        return dp[n-1]

            






















        