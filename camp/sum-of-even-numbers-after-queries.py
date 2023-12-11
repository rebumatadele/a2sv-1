class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        even_sum = []
        total = 0
        for k in nums:
            if k%2==0:
                total +=k
        for lst in queries:
            if nums[lst[1]] %2 == 0:
                    total = total - nums[lst[1]]
            nums[lst[1]]+=lst[0]
            if (nums[lst[1]]) %2 ==0:
                total += nums[lst[1]]    
            even_sum.append(total)
        return even_sum