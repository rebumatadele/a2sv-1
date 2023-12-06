class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        total = 0
        for i in range(n - 1):
            if total>1:
                return False
            elif nums[i] <=nums[i+1]:
                continue
            elif nums[i] < nums[i+1]:
                nums[i+1] = nums[i]
                total +=1
                continue
            
            elif nums[i]> nums[i+1] and i == 0:
                nums[i] = nums[i+1]
                total +=1
                continue
            elif nums[i]> nums[i+1] and i> 0 and nums[i+1] < nums[i-1]:
                nums[i+1] = nums[i]
                total +=1
                continue
            elif nums[i]> nums[i+1] and i> 0 and nums[i+1] >= nums[i-1]:
                nums[i] = nums[i+1]
                total +=1
            else:
                return False

                

        if total>1:
                return False
        return True