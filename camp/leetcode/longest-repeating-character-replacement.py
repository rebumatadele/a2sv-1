class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dic = {}
        freq = 0
        start = 0
        res = 0
        for end, char in enumerate(s):
            
            dic[char] = dic.get(char, 0) + 1 
            
            freq = max(freq, dic[char])
            if (end - start + 1) - freq > k:
                dic[s[start]] -= 1
                start += 1
            
            res = max(res, end-start+1)
        
        return res