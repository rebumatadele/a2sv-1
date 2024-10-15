class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        m_len = 1
        m_st = s[0]
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                if j-i+1 > m_len and s[i:j+1] == s[i:j+1][::-1]:
                    m_len = j-i+1
                    m_st = s[i:j+1]
        return m_st
        