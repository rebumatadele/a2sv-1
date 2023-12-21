class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        strs= "".join(map(str, digits))
        result = list(map(int, str(int(strs) + 1)))
        return(result)