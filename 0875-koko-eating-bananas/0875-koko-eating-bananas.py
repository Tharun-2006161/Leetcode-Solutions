class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def binary(m):
            c = 0
            for i in range(len(piles)):
                if m >= piles[i]:
                    c += 1
                elif m < piles[i]:
                    c += ((piles[i] // m))
                    if piles[i] % m != 0:
                        c += 1

            return c <= h

        i = 1
        j = max(piles)
        while i <= j:
            m = (i + j) // 2
            if binary(m):
                j = m - 1
            else:
                i = m + 1
        return i

