class Solution:
    def romanToInt(self, s: str) -> int:
        p={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        t=0
        for i in range(len(s)):
            if i+1<len(s) and p[s[i]]<p[s[i+1]]:
                t-=p[s[i]]
            else:
                t+=p[s[i]]
        return t