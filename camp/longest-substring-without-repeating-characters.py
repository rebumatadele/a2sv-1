class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        largest = 0
        dic = defaultdict(int)
        for r in range(len(s)):
            dic[s[r]] += 1
            while dic[s[r]] >1:
                dic[s[left]] -=1
                left +=1
            largest = max(largest, (r - left) + 1) 
        return largest