class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        p=numBottles
        q=numBottles
        while q>=numExchange:
            n=q//numExchange
            p+=n
            q=n+(q%numExchange)
        return p