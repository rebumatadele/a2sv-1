class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = defaultdict(int)
        i = 0
        cur_len = 0
        res = 0
        for j in range(len(s)):
            dic[s[j]] += 1
            cur_len = j - i + 1
            maxFreq = max(dic.values())
            if cur_len - maxFreq > k:
                dic[s[i]] -= 1
                i += 1
                cur_len = j - i + 1
            res = max(res, cur_len)
        return res