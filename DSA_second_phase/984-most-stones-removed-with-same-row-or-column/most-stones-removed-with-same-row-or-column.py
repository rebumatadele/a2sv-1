class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        def build():
            heap = []
            dic = defaultdict(list)
            for i, val in enumerate(stones):
                for j in range(i+1, len(stones)):
                    if val[0] == stones[j][0] or val[1] == stones[j][1]:
                        dic[i].append(j)

            for key, val in dic.items():
                heappush(heap, (key, val))
            return heap

        def find(k):
            while k != parent[k]:
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

        heap = build()
        n = len(stones)
        parent = {i:i for i in range(len(stones))}
        size = [1 for _ in range(len(stones))]

        while heap:
            i, val = heappop(heap)
            for v in val:
                union(i, v)
        s = set()
        for key, val in parent.items():
            s.add(find(val))
        return len(stones) - len(s)

        




