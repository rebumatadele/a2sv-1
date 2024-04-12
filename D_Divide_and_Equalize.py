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

#Merge Sort Conquerer
def merge(left_half, right_half):
    left_index = 0
    right_index = 0
    sorted_array = []
 
    while left_index < len(left_half) and right_index < len(right_half):
        if left_half[left_index] <= right_half[right_index]:
            sorted_array.append(left_half[left_index])
            left_index += 1
        else:
            sorted_array.append(right_half[right_index])
            right_index += 1

    sorted_array.extend(left_half[left_index:])
    sorted_array.extend(right_half[right_index:])

    return sorted_array

#Merge Sort Divider Function
def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)

# Helper Function for binary search
def binary_helper(arr, pos, condition):
    total = 0
    test = 0
    for i in arr:
        test += ceil(i/pos)
    if test <= condition:
        return True

#Binary Search           
def binary(arr):
    left = 0
    right = max(arr)
    while left + 1 < right:
        mid = (left + right) // 2
        if binary_helper(arr, mid):
            right = mid
        else:
            left = mid
    return right

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
def gcd(a, b):
 if b == 0:
    return a
 return gcd(b, a % b)

#execution starts here
def solve():
    
    return
#accepting test cases   
t = i()
for i in range(t):
    solve()