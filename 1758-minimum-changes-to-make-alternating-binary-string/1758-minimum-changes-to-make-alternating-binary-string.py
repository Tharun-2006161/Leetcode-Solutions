class Solution:
    def minOperations(self, s: str) -> int:
        i=0
        c=0
        while i<len(s)-1:
            if s[i]==s[i+1]:
                c+=1
                i+=2
            else:
                i+=1
        return c