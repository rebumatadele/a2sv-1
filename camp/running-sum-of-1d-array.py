class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        total = 0
        lst = []
        for i in nums:
            total +=i
            lst.append(total)
        return lst