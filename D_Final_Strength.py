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
    sor_arr = [0] * len(sorted_array)
    l = 0
    r = 0
    while r < len(right_half):
        if l > 0 and sor_arr[i] == 0:
            sor_arr[l] = sor_arr[-1]
        if left_half[l] > right_half[r]:
            sor_arr[l] = r + 1
            r += 1
        else:
            l += 1
      
    r = 0
    l = 0      
    while l < len(left_half):
        if r > 0 and sor_arr[len(left_half) - 1 + i] == 0:
            sor_arr[len(left_half) - 1 + r] = sor_arr[-1]
        if left_half[l] < right_half[r]:
            sor_arr[len(left_half) - 1 + r] = r + 1
            l += 1
        else:
            r += 1
    print(sor_arr, l, r)
            
            
    
    
    return sorted_array

#Merge Sort Divider Function
def mergeSort(left, right, arr):
    if left == right:
        return [arr[left]]
    
    mid = left + (right - left) // 2
    left_half = mergeSort(left, mid, arr)
    right_half = mergeSort(mid + 1, right, arr)

    return merge(left_half, right_half)



#execution starts
def solve():
    iteration = int(sys.stdin.readline().strip())
    arr = l()
    new_arr = []
    for i, val in enumerate(arr):
        new_arr.append((val, i))
    mergeSort(0, len(arr)-1, arr)
    return
    
t = i()
for i in range(t):
    solve()