class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        max_ = sum(nums[:k])
        left = 1
        # right = k 
        current = max_
        # while right < len(nums):
        #     current = (current - nums[left-1] + nums[right])
        #     max_ = max(current, max_)
        #     left +=1
        #     right +=1
        for i in range(k, len(nums)):
            current = (current - nums[left-1] + nums[i])
            max_ = max(current, max_)
            left +=1
        return max_/k
