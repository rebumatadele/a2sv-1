class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        temp = x ^ y
        count = 0
        while temp > 0:
            count += temp & 1
            temp >>= 1
        return count
