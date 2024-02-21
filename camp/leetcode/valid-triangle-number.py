class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        # The sum of the two sides should be greater than the third side
        nums.sort()
        count = 0
        for right in range(len(nums) - 1, 1, -1):
            left = 0
            for mid in range(right - 1, 0, -1):
                
                while left < mid:
                    if nums[left] + nums[mid] > nums[right]:
                        count += mid - left
                        break
                    left += 1
        return count