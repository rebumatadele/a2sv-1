class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        max_ = len(nums)//3
        counter = 0
        max_list = []
        for i, value in enumerate(nums):
            counter = 1
            if value in max_list:
                continue
            for j in range(i+1, len(nums)):
                if value == nums[j]:
                    counter +=1
            if counter > max_:
                max_list.append(value)
        return max_list



 
        