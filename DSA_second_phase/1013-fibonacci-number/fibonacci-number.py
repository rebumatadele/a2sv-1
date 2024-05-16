class Solution:
    def fib(self, n: int) -> int:
        que = deque([0, 1])
        if n<2:
            return n
        for i in range(2, n+1):
            que.append(sum(que))
            que.popleft()
        return que[-1]
