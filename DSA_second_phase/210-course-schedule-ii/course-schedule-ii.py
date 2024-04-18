class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #a depends on b
        #build the graph


        graph = defaultdict(list)
        indegre = defaultdict(int)
        for i in range(numCourses):
            indegre[i] = 0

        for val in prerequisites:
            graph[val[1]].append(val[0])
            indegre[val[0]] += 1

        root = []
        for key, val in indegre.items():
            if val == 0:
                root.append(key)
        print(graph, root)

        que = deque(root)
        res = []
        while que:
            current = que.popleft()
            res.append(current)
            for ne in graph[current]:
                indegre[ne] -= 1
                degre = indegre[ne]
                if degre == 0:
                    que.append(ne)
        if len(res) != numCourses:
            return []
        return res

            
