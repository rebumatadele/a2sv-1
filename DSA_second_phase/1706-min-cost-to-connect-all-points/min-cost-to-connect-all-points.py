class Solution:        
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
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
                    size[root1] += 1
                return True
            return False


        heap = []
        for i,  val in enumerate(points):
            for j in range(i+1, len(points)):
                dist = abs(val[0]- points[j][0]) + abs(val[1]- points[j][1])
                heappush(heap, (dist, i, j))  
        # print(heap)
        n = len(points)
        parent = {i:i for i in range(n)}
        size = [1 for _ in range(n)]
    

        count = 0
        cost = 0
        while heap and count <= n:
            c, i, j = heappop(heap)
            if union(i, j):
                count += 1
                cost += c
        return cost
            