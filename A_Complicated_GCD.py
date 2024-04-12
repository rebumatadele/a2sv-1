import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil, sqrt, gcd
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
    return is_prime
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
def is_prime(x: int) -> bool:
    d = 2
    while d*d <= x:
        if x % d == 0:
            return False
        d += 1
    return True

def factor(n):
    factors = []
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            factors.append(i)
            if i != n // i:
                factors.append(n // i)
    return factors

#finding GCF from a list
def find_gcf(numbers):
    if len(numbers) == 0:
        return None
    gcf = numbers[0]
    for num in numbers[1:]:
        gcf = gcd(gcf, num)
    return gcf 

#finding lcm
def find_lcm(numbers):
    if len(numbers) == 0:
        return None
    lcm = numbers[0]
    for num in numbers[1:]:
        lcm = lcm * num // gcd(lcm, num)
    return lcm

#finding gcd manually
def custom_gcd(a, b):
 if b == 0:
    return a
 return custom_gcd(b, a % b)

#execution starts here
def solve():
    
    return
#accepting test cases   
numbers = l()
diff = numbers[1] - numbers[0]
if diff >=3:
    print(1)
else:
    numbers = [i for i in range(numbers[0], numbers[1] + 1)]
    print(find_gcf(numbers))
    
    
    
    
    
    
    
    
    
    
    
    
 