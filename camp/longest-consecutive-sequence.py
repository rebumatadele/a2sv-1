class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        counter = 1
        nums.sort()
        print(nums)
        temp = 1
        if len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1
        for i in range(len(nums) - 1) :
            if nums[i] == nums[i+1] - 1:
                temp += 1
            elif nums[i] == nums[i+1]:
                continue
            else:
                counter = max(counter, temp)
                temp = 1
            counter = max(counter, temp)
        return counter
