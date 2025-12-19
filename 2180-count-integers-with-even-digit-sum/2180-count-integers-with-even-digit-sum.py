class Solution:
    def countEven(self, num: int) -> int:
        def fun(a):
            sum=0
            while a>0:
                r=a%10
                sum=sum+r
                a=a//10
            return sum
        c=0
        for i in range(1,num+1):
            if fun(i)%2==0:
                c+=1
        return c
