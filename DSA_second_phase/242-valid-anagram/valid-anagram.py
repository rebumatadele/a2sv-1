class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if len(s) != len(t):
        #     return False
        # char_count_s = Counter(s)
        # char_count_t = Counter(t)
        # for key, val in char_count_s.items():
        #     if val != char_count_t[key]:
        #         return False
        # return True
        return sorted(s) == sorted(t)