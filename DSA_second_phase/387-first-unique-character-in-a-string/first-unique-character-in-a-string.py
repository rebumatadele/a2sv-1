class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = Counter(s)
        for i, el in enumerate(s):
            if char_map[el] == 1:
                return i
        return -1
