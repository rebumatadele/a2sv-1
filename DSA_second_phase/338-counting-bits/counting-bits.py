class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [0 for _ in range(n+1)]
        for i in range(n+1):
            count = 0
            j = i
            while j > 0:
                count += j & 1
                j >>= 1
            ans[i] = count
        return ans



                
                
