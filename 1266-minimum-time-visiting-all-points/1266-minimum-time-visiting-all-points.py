class Solution:
    def minTimeToVisitAllPoints(self, points: list[list[int]]) -> int:
        
        s = 0
        for (x1, y1), (x2, y2) in zip(points, points[1:]):
            s += max(abs(x2 - x1), abs(y2 - y1))
        return s