class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mi = prices[0]
        p = 0
        for i in range(len(prices)):
            mi = min(mi, prices[i])
            p = max(p, prices[i] - mi)
        
        return p
