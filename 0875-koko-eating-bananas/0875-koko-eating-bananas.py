class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def binary(m):
            c = 0
            for i in range(len(piles)):
                if piles[i] <= m:
                    c += 1
                elif piles[i] > m:
                    c += (piles[i] // m)
                    if piles[i] % m != 0:
                        c += 1
            return c <= h
        l = 1
        r = max(piles)
        
        while l <= r:
            m = (l + r) // 2
            if binary(m):
                r = m - 1
            else:
                l = m + 1
        return l
        
