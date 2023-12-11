class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        
        for i in range(left, right+1):
            for rang in ranges:
                if rang[0]<=i<=rang[1]:
                    break
            else:
                return False
        return True