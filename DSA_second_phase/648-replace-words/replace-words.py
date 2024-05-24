class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
    def addWord(self, word):
        current = self
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode()
            current = current.children[c]
        current.is_end = True

class Solution:
    def __init__(self):
        self.root = TrieNode()

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        current = self.root
        for word in dictionary:
            current.addWord(word)
        sent = sentence.split()

        ans = []
        for val in sent:
            current = self.root
            temp = ""
            for v in val:
                if v in current.children:
                    temp += v
                    current = current.children[v]
                # else:
                    if current.is_end:
                        ans.append(temp)
                        break
                else: 
                    ans.append(val)
                    break
            else:
                ans.append(val)
        ret = " ".join(ans)
        print(ret)
        return ret


