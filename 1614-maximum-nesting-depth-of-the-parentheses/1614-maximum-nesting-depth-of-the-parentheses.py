class Solution:
    def maxDepth(self, s: str) -> int:
        ma = 0
        c = 0
        for i in range(len(s)):
            if s[i] == ")":
                ma = max(ma, c)
                c -= 1
            elif s[i] == "(":
                c += 1
        return ma