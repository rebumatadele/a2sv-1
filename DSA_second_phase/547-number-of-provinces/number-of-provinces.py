class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def build():
            graph = defaultdict(list)
            for i, val in enumerate(isConnected):
                count = 1
                temp = []
                for j in val:
                    if j:
                        temp.append(count)
                    count += 1
                graph[i+1] = temp
            return graph

        def dfs(key):
            visited[key -1] = True
            # print(key)
            for neighbour in graph[key]:
                if not visited[neighbour -1]:
                    dfs(neighbour)
        
        graph = build()
        print(graph)
        visited = [False for _ in range(len(graph))]
        count = 0
        for val in graph.values():
            for i in val:
                if not visited[i-1]:
                    dfs(i)
                    count += 1
        return count
            # if not visited()


