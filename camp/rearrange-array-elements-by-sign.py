class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive = []
        negative = []
        polar_nums = []
        for i, value in enumerate(nums):
            if value>0:
                positive.append(value)
            elif value<0:
                negative.append(value)
        
        for i in range(len(positive)):
            polar_nums.append(positive[i])
            polar_nums.append(negative[i])
        return polar_nums
