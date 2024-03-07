class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def helper(pos):
            a = 0
            for i in nums:
                a += ceil(i/pos)
                if a > threshold:
                    return False
            return True
        left = 0
        right = max(nums) * threshold + 1
        while left + 1 < right:
            mid = (left + right) // 2
            if helper(mid):
                right = mid
            else:
                left = mid
        return right