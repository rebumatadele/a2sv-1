class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for indx, el in enumerate(nums):
            for jndx in range(indx + 1, len(nums)):
                if el + nums[jndx] == target:
                    return [indx, jndx]
        return []