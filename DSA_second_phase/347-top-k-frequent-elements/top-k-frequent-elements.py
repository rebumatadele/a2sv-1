class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        nums = list(set(nums))
        nums.sort(key = lambda x: dic[x], reverse = True)
        return nums[:k]