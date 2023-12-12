class Solution:
    def reverseWords(self, s: str) -> str:
        s.strip()
        s = s.split()
        for string in s:
            string.split()
        s = s[::-1]
        s = " ".join(s)
        return s