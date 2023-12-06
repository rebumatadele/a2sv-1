class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        sum = 0
        for i in range(1, len(points)):
          sum += max(abs(points[i][0] - points[i-1][0]),abs(points[i][1] - points[i-1][1]))
        return sum