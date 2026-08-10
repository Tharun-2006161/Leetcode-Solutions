class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        for i in asteroids:
            while res and i < 0 and res[-1] > 0:
                if abs(i) > res[-1]:
                    res.pop()
                    continue
                elif abs(i) == res[-1]:
                    res.pop()
                i = 0
                break
            if i != 0:
                res.append(i)
        return res