class Solution:
    def numTrees(self, n: int) -> int:
        def fact(n):
            res=1
            for i in range(1,n+1):
                res*=i
            return res
        return fact(2*n) // (fact(n+1) * fact(n))