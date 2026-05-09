class Solution:
    def isValid(self, s: str) -> bool:
        p="({["
        a=[]
        for i in s:
            if i in p:
                a.append(i)
            elif i==')' and a and a[-1]=="(":
                a.pop()
            elif i=="}" and a and a[-1]=="{":
                a.pop()
            elif i=="]" and a and a[-1]=="[":
                a.pop()
            else:
                return False
        if len(a)==0:
            return True
        else:
            return False

