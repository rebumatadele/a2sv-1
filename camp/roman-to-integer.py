class Solution:
    def romanToInt(self, s: str) -> int:
        dictionary = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        num = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and dictionary[s[i]] < dictionary[s[i + 1]]:
                num += dictionary[s[i + 1]] - dictionary[s[i]]
                i += 2
            else:
                num += dictionary[s[i]]
                i += 1

        return num