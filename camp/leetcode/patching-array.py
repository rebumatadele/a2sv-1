class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        current = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] > n:
                break
            while current < nums[i] -1:
                current += current + 1
                count += 1
            current += nums[i]
        while n > current:
            current += current + 1
            count += 1
        return count
            


            