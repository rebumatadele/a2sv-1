class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                if n % d == 0:
                    while n % d == 0:
                        n //= d
                    factors.add(d)
                d += 1
            if n > 1:
                factors.add(n)
            return factors
        distinct_factors = set()
        for num in nums:
            factors = prime_factors(num)
            distinct_factors.update(factors)

        return len(distinct_factors)