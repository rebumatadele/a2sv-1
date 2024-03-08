class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i in range(len(nums) * 2):
            while stack and nums[i % len(nums)] > nums[stack[-1]]:
                ans[stack.pop()] = nums[i % len(nums)]
            stack.append(i % len(nums))   
        return ans     
