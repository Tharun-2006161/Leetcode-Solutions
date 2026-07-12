class Solution:
    def totalMoney(self, n: int) -> int:
        c = 0
        res = 0
        if n<=7:
            return n*(n+1)//2
        qu = n//7
        # print(qu)
        # if qu==1:
        #     res+=28
        # else:
        #     res+=((qu*28)+((qu-1)*7))
        # print(n%7)
        t = 28
        e=qu
        while e>0:
            res+=t
            t+=7
            e-=1
        print(res)
        for i in range(1,(n%7)+1):
            res+=(qu+i)
        return res
