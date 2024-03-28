class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        size = len(nums)
        i = 0
        while i < size:
            if nums[i] < 0 or nums[i] == i + 1:
                i += 1
            elif nums[i] == nums[nums[i] -1]:
                nums[i] = -1
            else:
                curr = nums[i] - 1
                nums[i], nums[curr] = nums[curr], nums[i]
        res = []
        for i in range(len(nums)):
            if nums[i] < 0:
                res.append(i+1)
        return res