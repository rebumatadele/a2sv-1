class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min_ = nums[0]
        max_ = float('inf')
        for i in range(1, len(nums)):
            if nums[i]> min_ and nums[i] < max_:
                max_=nums[i]
            if nums[i] < min_:
                min_ = nums[i]
            if nums[i] > max_:
                return True
        
        