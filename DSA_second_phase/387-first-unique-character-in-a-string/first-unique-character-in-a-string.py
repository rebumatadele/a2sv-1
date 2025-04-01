class Solution:
    def firstUniqChar(self, s: str) -> int:
        char_map = defaultdict(int)
        for el in s:
            char_map[el] += 1
        i = 0
        print(char_map)
        for value in s:
            if char_map[value] == 1:
                return i
            i += 1
        return -1
