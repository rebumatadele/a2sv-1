class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        right = s.count("(")
        defeciet = 0
        count = 0
        for i in s:
            if i == "(":
                defeciet += 1
            else:
                defeciet -= 1
            if defeciet < 0:
                defeciet += 1
                count += 1 
        count += defeciet
        return count
