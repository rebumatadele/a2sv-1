class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = deque()
        #we want a monotonic strictly decreasing que
        res = []
        count = 0
        for i, val in enumerate(nums):
            count += 1
            if que and ((i - que[0][0]) + 1) > k:
                que.popleft()
            while que and val > que[-1][1]:
                que.pop()
            que.append((i, val))
            if count >= k:
                res.append(que[0][1])
        return res
