class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n=len(cost)
        cost.sort(reverse=True)
        c=0
        if len(cost)==1:
            return cost[0]
        if len(cost)>3:
            for i in range(0,len(cost)-1,3):
                c+=(cost[i]+cost[i+1])
            if n%3==1:
                c+=cost[-1]
            return c
        else:
            return cost[0]+cost[1]
        