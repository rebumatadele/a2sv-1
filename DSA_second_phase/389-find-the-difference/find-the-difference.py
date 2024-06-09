class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        os = 0
        ot = 0
        for val in s:
            os += ord(val)
        for val in t:
            ot += ord(val)
        return chr(ot - os)
        