class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for x in nums:
            count[x] += 1
        for key, val in count.items():
            if val == 1:
                return key
        return -1