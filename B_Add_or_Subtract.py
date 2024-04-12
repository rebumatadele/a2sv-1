def add_subtract():
    t = int(input())
    for _ in range(t):
        nums = input().split()
        nums = list(map(int, nums))
        if (nums[0] + nums[1] == nums[2] and nums[0] - nums[1] == nums[2]) ==False:
            if nums[0] + nums[1] == nums[2]:
                print("+")
            elif nums[0] - nums[1] == nums[2]:
                print("-")
add_subtract()