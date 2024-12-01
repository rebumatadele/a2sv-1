class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_store = defaultdict(int)
        for indx, el in enumerate(nums):
            difference = target - el
            if difference in nums_store.keys():
                return [nums_store[difference], indx]
            nums_store[el] = indx
        return []