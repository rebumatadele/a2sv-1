# n = int(input())
# max_=0
# for i in range(n):
#     w, h = map(int, input().split())
#     if i == 0:
#        max_=max(w, h)
#     if h > max_ and w > max_:
#         print("NO")
#         break
#     if max(h, w) <= max_:
#         max_= max(h, w)
#     else:
#         max_ = min(h, w)
# else:
#     print("YES")
def counting_sort(arr):
    # Find the maximum element in the input array
    max_value = max(arr)
    
    # Create a count array to store the counts of each element
    count = [0] * (max_value + 1)
    
    # Count the occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Calculate the prefix sums in the count array
    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    # Create a sorted output array
    sorted_arr = [0] * len(arr)
    
    # Place each element in its correct position in the sorted array
    for num in arr:
        sorted_arr[count[num] - 1] = num
        count[num] -= 1
    
    return sorted_arr




def pancake_sort(arr):
    def flip(sublist, k):
        i = 0
        while i < k / 2:
            sublist[i], sublist[k - i - 1] = sublist[k - i - 1], sublist[i]
            i += 1
    
    def find_max_index(arr, n):
        max_index = 0
        for i in range(1, n):
            if arr[i] > arr[max_index]:
                max_index = i
        return max_index
    
    n = len(arr)
    while n > 1:
        max_index = find_max_index(arr, n)
        
        # Move the max element to the beginning
        flip(arr, max_index + 1)
        
        # Move the max element to the end
        flip(arr, n)
        
        n -= 1
    
    return arr