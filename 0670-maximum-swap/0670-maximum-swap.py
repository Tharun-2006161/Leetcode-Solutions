class Solution:
    def maximumSwap(self, num: int) -> int:
        p = list(str(num))
        temp = p
        res = num
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                p[i] , p[j] = p[j] , p[i]
                res = max(res , int("".join(p)))
                p[j] , p[i] = p[i] , p[j]
        return res