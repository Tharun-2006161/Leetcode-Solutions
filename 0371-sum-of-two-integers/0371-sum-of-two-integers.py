class Solution:
    def getSum(self, a: int, b: int) -> int:
        m=0xffffffff
        while b:
            s=(a^b)&m
            c=((a&b)<<1)&m
            a=s
            b=c
        if a>0x7fffffff:
            a=~(a^m)
        return a