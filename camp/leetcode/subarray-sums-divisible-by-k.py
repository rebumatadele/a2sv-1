class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        current = 0
        counter = Counter()
        for num in nums:
            current = (current + num) % k
            counter[current] += 1
        res = 0
        for i in counter:
            res += counter[i]*(counter[i]-1)//2
        return res + counter[0]            
            
        