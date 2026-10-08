class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        i = 0
        j = 0
        c = 0
        res = ""
        while i < len(s) and j < len(s):
            if s[j] == "(":
                c += 1
            elif s[j] == ")":
                c -= 1
            if c == 0:
                res += s[i + 1:j]
                i = (j + 1)
            j += 1
        return res
            
