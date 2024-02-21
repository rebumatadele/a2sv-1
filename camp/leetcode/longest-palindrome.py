class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = defaultdict(int)
        flag = 0
        count = 0

        for i in s:
            dic[i] += 1

        for key, val in dic.items():       
            flag += val % 2
            if val % 2 == 1:
                val -= 1
            count += val
        if flag:
            count += 1
        return count
