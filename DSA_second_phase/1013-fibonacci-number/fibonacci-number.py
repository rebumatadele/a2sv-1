class Solution:
    def fib(self, n: int) -> int:
        que = deque([0, 1])
        ans = 1
        if n == 0 or n == 1:
            return n
        for i in range(2, n+1):
            ans = sum(que)
            que.append(ans)
            que.popleft()
        return ans
