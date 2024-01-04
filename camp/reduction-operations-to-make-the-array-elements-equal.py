class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        from collections import defaultdict
        num = set(nums)
        count = 1
        dic = defaultdict(int)
        lst = list(num)
        lst.sort(reverse = True)
        print(lst)
        for i in range(len(lst)):
            dic[lst[i]] = len(lst) - count
            count +=1
        total = 0
        for i in range(len(nums)):
            total += dic[nums[i]]
        return total
