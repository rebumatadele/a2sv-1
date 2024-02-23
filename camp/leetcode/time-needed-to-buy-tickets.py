class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        #lets build the que
        q = deque()
        for i, val in enumerate(tickets):
            q.append((i, val))
        time = 0
        while q:   
            curr = q.popleft()
            if curr[0] == k and curr[1] == 1:
                time += 1
                break
            if curr[1] == 1:
                time += 1
                continue
            else:
                q.append((curr[0], curr[1]-1))
            time += 1
        return time
            


