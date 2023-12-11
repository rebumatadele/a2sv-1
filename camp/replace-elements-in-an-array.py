class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        my_dict = {}
        operations = reversed(operations)
        for x, y in operations:
            my_dict[x] = my_dict.get(y, y)
        for idex, val in enumerate(nums):
            if val in my_dict:
                nums[idex] = my_dict[val]
        return nums