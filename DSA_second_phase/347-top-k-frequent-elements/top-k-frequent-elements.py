class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = defaultdict(int)
        for i in nums:
            dic[i] += 1
            
        my_nums = []
        for key, val in dic.items():
            my_nums.append((val, key))

        heap = []
        for i in my_nums:
            heappush(heap, i)
            if len(heap) > k:
                heappop(heap)
        ans = []
        for i in heap:
            ans.append(i[1])

        return sorted(ans)