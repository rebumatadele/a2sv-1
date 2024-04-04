class Solution:
    def smallestValue(self, n: int) -> int:
        def prime_factor(n):
            factorization: list[int] = []
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factorization.append(d)
                    n //= d
                d += 1
            if n > 1:
                factorization.append(n)
            return factorization
        # print(prime_factor)
        while len(prime_factor(n)) > 1:
            k = sum(prime_factor(n))
            if n == k:
                break
            n = k
        return n