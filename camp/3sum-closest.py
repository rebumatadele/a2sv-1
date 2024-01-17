class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_sum = float('inf')
        min_diff = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                curr_sum = nums[i] + nums[left] + nums[right]
                diff = abs(curr_sum - target)
                if diff < min_diff:
                    min_diff = diff
                    closest_sum = curr_sum
                if curr_sum < target:
                    left += 1
                else:
                    right -= 1
        return closest_sum