class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_consec=0
        temp = 0
        for i in nums:
            if i == 0:
                max_consec = max(max_consec, temp)
                temp=0
                continue
            elif i==1:
                temp+=1
            
        max_consec = max(max_consec, temp)
        return max_consec