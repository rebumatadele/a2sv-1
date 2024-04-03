class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def build(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u) 
            return graph
        
        def dfs(vertex, visited):
            if vertex == destination:
                return True
            visited.add(vertex)
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    node = dfs(neighbour, visited)
                    if node:
                        return True

        visited = set()
        graph = build(edges)
        print(graph)
        return dfs(source, visited)