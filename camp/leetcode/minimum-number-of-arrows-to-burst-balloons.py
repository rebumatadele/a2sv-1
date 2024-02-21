class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[0])
        current = points[0][1]
        count = 1
        for i in range(1, len(points)):
            if points[i][0] <= current and points[i][1] >= current:
                continue
            elif points[i][0] <= current and points[i][1] < current:
                current = points[i][1]
                continue
            count += 1
            current = points[i][1]
        return count

