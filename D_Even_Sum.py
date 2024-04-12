def even_sum():
    n = int(input())
    nums = input().split()
    nums = list(map(int, nums))
    od = 0
    nums = sorted(nums)
    if sum(nums) % 2 == 0:
        print(sum(nums))
    for i in nums:
        if i % 2 ==1:
            od = i
            break
    if sum(nums) % 2 ==1:
        print(sum(nums) - od)
even_sum()