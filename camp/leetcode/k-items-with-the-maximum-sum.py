class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if k <= numOnes + numZeros:
            return min(k, numOnes)
        else:
            temp = min(k, numOnes)
            num = k - (numOnes + numZeros)
            return temp - num