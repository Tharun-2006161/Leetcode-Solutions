class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        c=0
        st=""
        for i in s:
            if i==")":
                c-=1
            if c!=0:
                st+=i
            if i=="(":
                c+=1
        return st