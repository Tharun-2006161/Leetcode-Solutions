class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x=""
        su=0
        s=str(n)
        for i in range(len(s)):
            if s[i]!="0":
                x+=s[i]
        if x=='':
            return 0
        print(x)
        nn=int(x)
        r=nn
        while nn>0:
            t=nn%10
            su=su+t
            nn=nn//10
        print(su)      
        return (su*r)
