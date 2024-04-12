class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        que = deque([("0000", 0)])
        dead = set(deadends)
        visited = set(["0000"])

        cnt = 0
        def getDxn(current, digit):
            return [current[:i] + str((digit + 1) % 10) + current[i+1:],
                    current[:i] + str((digit - 1) % 10) + current[i+1:]
                    ]

        while que:
            current, steps = que.popleft()
            if current == target:
                return steps

            if current not in dead:  
                for i in range(4):
                    nxt = getDxn(current, int(current[i]))

                    for comb in nxt:
                        if comb not in visited:
                            visited.add(comb)
                            que.append((comb, steps + 1))
        return -1
