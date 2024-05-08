class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        inDegrees = [0] * n
        adj = defaultdict(list)
        for a, b in richer:
            adj[a].append(b)
            inDegrees[b] += 1

        res = [e for e in range(n)]
        quietest = quiet[::]

        q = deque([i for i, degree in enumerate(inDegrees) if degree == 0])

        while q:
            cur = q.popleft()

            for out in adj[cur]:
                if quietest[cur] < quietest[out]:
                    quietest[out] = quietest[cur]
                    res[out] = res[cur]
                inDegrees[out] -= 1
                if inDegrees[out] == 0:
                    q.append(out)
        return res