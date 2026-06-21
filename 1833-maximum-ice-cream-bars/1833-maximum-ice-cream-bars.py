class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        s=max(costs)
        cs=[0]*(s+1)
        for i in range(len(costs)):
            cs[costs[i]-1]+=1
        res=0
        for i in range(len(cs)):
            if cs[i]>0:
                if (coins//(i+1) >= cs[i]):
                    coins=coins-(cs[i]*(i+1))
                    res+=cs[i]
                    if coins <(i+1):
                        break
                else:
                    res+=(coins//(i+1))
                    break
        return res
