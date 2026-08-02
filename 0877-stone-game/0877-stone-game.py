class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        
        @cache
        def dp(l, r):
            if l == r:
                return piles[l]
            left = (piles[l] - dp(l + 1, r))
            right = (piles[r] - dp(l, r - 1))
            return max(left, right)

        n = len(piles)
        return dp(0, n - 1) > 0