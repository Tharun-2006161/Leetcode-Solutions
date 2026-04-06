class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        MOD = 10**9 + 7
        p=[True]*(n+1)
        p[0]=p[1]=False
        for i in range(2,int(n**0.5) + 1):
            if p[i]:
                for j in range(i*i,n+1,i):
                    p[j]=False
        s=sum(p)
        a=n-s
        def fun(a):
            res=1
            for i in range(1,a+1):
                res=(res*i)%MOD
            return res
        return (fun(s)*fun(a))%MOD