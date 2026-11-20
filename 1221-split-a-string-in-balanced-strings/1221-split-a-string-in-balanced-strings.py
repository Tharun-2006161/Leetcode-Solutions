class Solution:
    def balancedStringSplit(self, s: str) -> int:
        i = 0
        rc = 0
        lc = 0
        ans = 0 
        while i < len(s):
            if s[i] == "R":
                rc += 1
            elif s[i] == "L":
                lc += 1
            if rc == lc:
                ans += 1
            i += 1
        return ans
