class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        from collections import defaultdict
        count_1 = 0
        for num in nums:
            if num == 1: count_1 += 1
        
        count_0 = 0
        max_div = count_1
        dic = defaultdict(list)
        dic[count_1].append(0)
        for i, num in enumerate(nums):
            count_0 += int(num == 0)
            count_1 -= int(num == 1)
            dic[count_0 + count_1].append(i + 1)
            max_div = max(max_div, count_0 + count_1)
        return dic[max_div]
