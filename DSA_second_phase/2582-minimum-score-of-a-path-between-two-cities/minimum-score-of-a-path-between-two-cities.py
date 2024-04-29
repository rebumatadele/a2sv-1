class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        
        def find(k):
            while parent[k] != k:
                parent[k] = parent[parent[k]]
                k = parent[k]
            return k
        def union(x, y):
            root1 = find(x)
            root2 = find(y)
            if root1 != root2:
                if size[root1] > size[root2]:
                    parent[root2] = root1
                elif size[root2] > size[root1]:
                    parent[root1] = root2
                else:
                    parent[root2] = root1
                    size[root1] += root2

        parent = {i:i for i in range(n + 1)}
        size = [1 for _ in range(n + 1)]
        score = float("inf")
        
        for val in roads:
            union(val[0], val[1])
        for val in roads:
            root1 = find(1)

            rootx = find(val[0])
            rooty = find(val[1])
            if root1 == rootx == rooty:
                score = min(score, val[2])
        return score


        