import sys
def i(): return int(sys.stdin.readline().strip())
def l(): return list(map(int, sys.stdin.readline().strip().split()))
def ls(): return sorted(list(map(int, sys.stdin.readline().strip().split())))
def s(): return sys.stdin.readline().strip()
def d(): return [int(digit) for digit in input()]
def c(): return list(sys.stdin.readline().strip())

from collections import Counter, defaultdict, deque
from bisect import bisect_right, bisect_left
from math import ceil

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
def helper(arr, pos, condition):
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
        if helper(arr, mid):
            right = mid
        else:
            left = mid
    return right

#execution starts
def solve():
    
    return
    
t = i()
for i in range(t):
    solve()