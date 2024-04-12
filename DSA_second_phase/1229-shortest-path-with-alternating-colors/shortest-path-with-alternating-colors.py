class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = [ [[] , []] for _ in range(n) ]

        for x, y in blueEdges:
            graph[x][0].append(y)
        for x, y in redEdges:
            graph[x][1].append(y)

        dis = 0
        que = deque([(0, 0), (0, 1)])
        visited = set([(0, 0), (0, 1)])
        answer = [-1 for _ in range(n)]

        while que:
            for _ in range(len(que)):
                current, color = que.popleft()
                if answer[current] == -1:
                    answer[current] = dis
                turn = 1 - color
                for neighbor in graph[current][turn]:
                    if (neighbor, turn) not in visited:
                        visited.add((neighbor, turn))
                        que.append((neighbor, turn))
            dis += 1
        print(answer)
        return answer



        