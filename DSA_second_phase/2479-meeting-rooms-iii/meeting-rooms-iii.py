class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        taken = []
        available = []
        start = 0
        count = defaultdict(int)
        meetings.sort()
        for i in range(n):
            heappush(available, i)


        for val in meetings:
            start = max(start, val[0])
            ending = (val[1] - val[0]) + start
            


            while (taken and taken[0][0] <= start):
                heappush(available, heappop(taken)[1])
            if not available:
                c = heappop(taken)
                heappush(available, c[1])
                start = c[0]
                ending = (val[1] - val[0]) + start


            current = heappop(available)
            count[current] += 1
            heappush(taken, (ending, current))



        print(count)
        room  = count
        minn = 0
        ans = 0
        count = -1
        for key, val in room.items():
            if val > minn:
                ans = key
                minn = val

        return ans

