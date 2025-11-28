class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = prices[0]
        maxi = 0
        for i in range(1,len(prices)):
            if prices[i]<min:
                min = prices[i]
            elif ((prices[i]-min)>maxi):
                maxi = prices[i]-min
        return maxi
