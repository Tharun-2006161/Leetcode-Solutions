class Solution:
    def longestPalindrome(self, s: str) -> int:
        p=Counter(s)
        t=list(p.values())
        e=[]
        o=[]
        for i in t:
            if i%2==0:
                e.append(i)
            else:
                o.append(i)
        return sum(e) + sum([x-1 for x in o])+(1 if o else 0)
