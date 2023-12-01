class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        good = 0
        for i in range(j+1):
            for k in range(i+1, j+1):
                if nums[i] == nums[k]:
                    good +=1
        return good


            