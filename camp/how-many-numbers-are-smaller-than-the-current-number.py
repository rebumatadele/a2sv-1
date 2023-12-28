class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst = sorted(nums)
        res = []
        for i in nums:
            res.append(lst.index(i))
        return res