class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = []
        i = 0
        j = 1
        while i < len(prices) and j < len(prices):
            if prices[j] > prices[i]:
                res.append(abs(prices[i] - prices[j]))
            i += 1
            j += 1
        return sum(res)