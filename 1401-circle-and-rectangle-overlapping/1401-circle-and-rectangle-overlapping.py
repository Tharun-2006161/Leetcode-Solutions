class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        
        t = max(x1, min(xCenter, x2))
        s = max(y1, min(yCenter, y2))

        return (xCenter - t) ** 2 + (yCenter - s) ** 2 <= radius ** 2