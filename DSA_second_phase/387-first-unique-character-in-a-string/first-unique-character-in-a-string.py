class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = Counter(s)
        for i, value in enumerate(s):
            if char_map[value] == 1:
                return i
        return -1
