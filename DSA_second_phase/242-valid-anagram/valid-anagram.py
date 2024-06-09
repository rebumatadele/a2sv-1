class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic = defaultdict(int)
        for val in s:
            dic[val] += 1
        for val in t:
            if dic[val]:
                dic[val] -= 1
            else:
                return False
        for val in dic.values():
            if val > 0:
                return False
        return True