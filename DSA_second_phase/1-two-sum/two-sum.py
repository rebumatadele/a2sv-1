class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_lst = []
        for idx, el in enumerate(nums):
            num_lst.append((el, idx))
        
        num_lst.sort()
        i = 0
        j = len(num_lst) - 1
        while i < j:
            current = num_lst[i][0] + num_lst[j][0]
            if current == target:
                return [num_lst[i][1], num_lst[j][1]]
            elif current > target:
                j -= 1
            else:
                i += 1
        