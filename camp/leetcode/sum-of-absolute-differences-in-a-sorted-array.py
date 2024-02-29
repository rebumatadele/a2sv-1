class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp1 = 0
        temp2 = 0
        for num in nums:
            temp2 += num
        res = [0] * n
        i = 0
        for num in nums:
            res[i] = (2 * i - n) * num + temp2 - temp1
            temp1 += num
            temp2 -= num
            i += 1
        return res

