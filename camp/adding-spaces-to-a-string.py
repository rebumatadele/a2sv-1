class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        last = 0
        result = ""
        for value in spaces:
            result += s[last:value]
            result += " "
            last = i=value
        result += s[last:]
        return result  