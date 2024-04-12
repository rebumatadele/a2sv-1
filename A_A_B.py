def a_plus_b():
    num = int(input())
    for _ in range(num):  
        string = input()
        nums = string.split("+")
        print(int(nums[0]) + int(nums[1]))
a_plus_b()