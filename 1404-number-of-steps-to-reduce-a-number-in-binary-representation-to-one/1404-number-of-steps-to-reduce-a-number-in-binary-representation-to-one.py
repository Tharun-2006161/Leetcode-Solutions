class Solution:
    def numSteps(self, s: str) -> int:
        p=int(s,2)
        c=0
        while p!=1:
            if p%2==0:
                p=p//2
                c+=1
            else:
                p+=1
                c+=1
        return c