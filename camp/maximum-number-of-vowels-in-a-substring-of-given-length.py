class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']

        first = s[:k]
        cnt = 0
        for i in first:
            if i in vowels:
                cnt += 1
        left = 0
        temp = cnt
        for right in range(k, len(s)):
            if s[right] in vowels:
                temp = temp + 1
            if s[left] in vowels:
                temp -= 1
            cnt = max(cnt, temp)
            left += 1
        return cnt




