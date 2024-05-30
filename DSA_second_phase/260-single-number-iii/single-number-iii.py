class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        r = xor & -xor
        group1, group2 = 0, 0
        for num in nums:
            if num & r:
                group1 ^= num
            else:
                group2 ^= num
        return [group1, group2]