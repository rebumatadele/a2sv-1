class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_pivot = []
        greater_pivot =[]
        equal_pivot = []
        new_nums = []
        for num in nums:
            if num > pivot:
                greater_pivot.append(num)
            elif num < pivot:
                less_pivot.append(num)
            else:
                equal_pivot.append(num)
        for i in range(len(nums)):
            if len(less_pivot)>i:
                new_nums.append(less_pivot[i])
        for i in range(len(nums)):
            if len(equal_pivot)>i:
                new_nums.append(equal_pivot[i])
        for i in range(len(nums)):
            if len(greater_pivot)>i:
                new_nums.append(greater_pivot[i])
        return new_nums
            
            

