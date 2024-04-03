class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
        def build(edges):
            graph = defaultdict(list)
            for u, v in edges:
                graph[u].append(v)
                graph[v].append(u) 
            return graph
        
        def dfs(visited, stack):

            while stack:
                current = stack.pop()
                if current == destination:
                    return True

                for neighbour in graph[current]:
                    if neighbour not in visited:
                        stack.append(neighbour)
                        visited.add(neighbour)

            return False
        visited = set()
        stack = [source]
        graph = build(edges)
        return dfs(visited, stack)