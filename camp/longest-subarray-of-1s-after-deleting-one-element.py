class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        cnt = 0
        left = 0
        total = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                cnt +=1
            while left <= i and cnt > 1:
                if nums[left] == 0:
                    cnt -=1
                left += 1
            total = max(total, i - left)
        return total
