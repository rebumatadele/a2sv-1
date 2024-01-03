class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i in range(len(nums) -1):
            if nums[i] == nums[i+1]:
                nums[i] = "_"
        print(nums)
        holder = 0
        seeker = 0
        while seeker < len(nums):
            if nums[seeker] == "_":
                seeker +=1
                continue
            elif nums[holder] == "_":
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
            holder +=1
            seeker +=1
        k = 0
        for i in nums:
            if i =="_" or i=="":
                break
            k +=1
        return(k)