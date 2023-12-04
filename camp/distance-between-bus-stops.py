class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        sol = 0
        if start < destination:
            sol = min(sum(distance[start:destination]), sum(distance[destination:]) + sum(distance[:start]))
        elif start > destination:
            sol = min(sum(distance[destination:start]), sum(distance[start:]) + sum(distance[:destination]))
        return sol

        

