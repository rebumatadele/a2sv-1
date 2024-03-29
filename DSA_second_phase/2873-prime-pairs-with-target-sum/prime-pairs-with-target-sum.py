class Solution:
    def findPrimePairs(self, n: int) -> List[List[int]]:
        def sieve(n):
            is_prime:list[bool] = [True for _ in range(n + 1)]
            is_prime[0] = is_prime[1] = False
            d = 2
            while d*d <= n:
                if is_prime[d]:
                    i = d * d
                    while i <= n:
                        is_prime[i] = False
                        i += d
                d += 1   
            ans = []
            for i, val in enumerate(is_prime):
                if val:
                    ans.append(i)      
            return ans
        factors = sieve(n)
        ans = []
        i = 0
        j = len(factors) -1
        while i <= j:
            if factors[i] + factors[j] == n:
                ans.append([factors[i], factors[j]])
                i += 1
                j -= 1
            elif factors[i] + factors[j] > n:
                j -= 1
            else:
                i += 1

        return ans
                

            