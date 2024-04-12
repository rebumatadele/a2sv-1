class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        goal = len(rooms)
        que = deque([0])
        visited = set([0])
        flag = 0
        while que:
            current = que.popleft()
            flag += 1
            if rooms[current]:
                for val in rooms[current]:
                    if val not in visited:
                        que.append(val)
                        visited.add(val)
        return goal == flag


