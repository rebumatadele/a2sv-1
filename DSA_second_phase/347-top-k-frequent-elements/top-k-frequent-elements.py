class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
        print(dic)
        nums = list(set(nums))
        nums.sort(key = lambda x: dic[x], reverse = True)
        print(nums)
        ans = []
        for i in nums:
            if not ans or ans[-1] != i:
                ans.append(i)
        return ans[:k]