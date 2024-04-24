class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        leaves = deque([i for i in range(n) if len(graph[i]) == 1])

        while n > 2:
            n -= len(leaves)
            new_leaves = deque()
            for leaf in leaves:
                current = graph[leaf].pop() 
                graph[current].remove(leaf)
                
                if len(graph[current]) == 1:
                    new_leaves.append(current)
            leaves = new_leaves

        return list(leaves)