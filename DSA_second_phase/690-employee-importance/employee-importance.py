"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        
        def build():
            graph = defaultdict(list)
            for i, val in enumerate(employees):
                temp = val.subordinates
                temp.append(val.id)
                graph[val.id] = temp
            return graph

        def dfs(key):
            visited.add(key)
            for neighbour in graph[key]:
                if neighbour not in visited:
                    dfs(neighbour)
        
        graph = build()
        visited = set()
        print(graph)
        val = graph[id]
        for key in val:
            if key not in visited:
                dfs(key)
        print(visited)
        ans = 0
        for val in employees:
            if val.id in visited:
                ans += val.importance
        return ans
