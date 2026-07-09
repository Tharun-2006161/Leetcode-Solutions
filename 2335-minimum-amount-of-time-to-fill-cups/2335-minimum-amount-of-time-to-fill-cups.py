class Solution:
    def fillCups(self, amount: List[int]) -> int:
        c=0
        amount.sort()
        while amount[1]>0 and amount[2]>0:
            amount[1]-=1
            amount[2]-=1
            c+=1
            amount.sort()
        while amount[2]>0:
            amount[2]-=1
            c+=1
        return c
