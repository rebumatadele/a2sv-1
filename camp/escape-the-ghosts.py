class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        my_speed = abs(target[0]) + abs(target[1])
        for ghost in ghosts:
            ghost_speed = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_speed <= my_speed:
                return False
        return True