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
    
    def removeWord(self, word):
        current = self
        current.count -= 1
        for c in word:
            if c in current.children:
                current = current.children[c]
                current.count -= 1

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        rows, cols = len(board), len(board[0])
        result, visit = set(), set()

        def dfs(r, c, node, word):
            if r not in range(rows) or c not in range(cols) or board[r][c] not in node.children or node.children[board[r][c]].count < 1 or (r, c) in visit:
                return
            
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.is_word:
                node.is_word = False
                result.add(word)
                root.removeWord(word)

            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)
            visit.remove((r, c))

        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")

        return list(result)
            
            
        
