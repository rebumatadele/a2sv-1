class Solution:
    def longestPalindrome(self, s: str) -> int:
        dic = defaultdict(int)
        flag = 0
        count = 0

        for i in s:
            dic[i] += 1

        for key, val in dic.items():
            if val % 2 == 1:
                flag += 1

            if flag > 1 and val % 2 == 1:
                count += val - 1
                continue

            count += val

        return count
