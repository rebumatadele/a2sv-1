class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        def dfs(vertex, visited, colors):
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour in visited:
                    if colors[vertex] == colors[neighbour]:
                        return False
                else:
                    colors[neighbour] = 1 - colors[vertex]
                    ret = dfs(neighbour, visited, colors)

                    if not ret:
                        return False
            return True
        n = len(graph)
        visited = set()
        colors = [-1] * n
        for i in range(n):
            if i not in visited:
                colors[i] = 0
                if not dfs(i, visited, colors):
                    return False
        return True