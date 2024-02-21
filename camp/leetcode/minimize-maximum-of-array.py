class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        
        maximum = nums[0]
        s = nums[0]
        for i in range(1, len(nums)):
            s = s + nums[i]
            size = i + 1
            av = ceil(s / size)
            maximum = max(av, maximum)
        return maximum