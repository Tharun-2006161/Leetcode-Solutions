class Solution:
    def maxPower(self, s: str) -> int:
        if len(s) == 1:
            return 1
        i = 0 
        j = 1
        ma = 0
        while i < len(s) and j < len(s):
            if s[i] == s[j]:
                j += 1
            elif s[i] != s[j]:
                ma = max(ma, j - i)
                i = j
                j += 1
            else:
                i += 1
                j += 1
        ma = max(ma, j - i)
        return ma
