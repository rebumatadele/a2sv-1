class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = defaultdict(int)
        for el in s:
            char_map[el] += 1
        for i, value in enumerate(s):
            if char_map[value] == 1:
                return i
            i += 1
        return -1
