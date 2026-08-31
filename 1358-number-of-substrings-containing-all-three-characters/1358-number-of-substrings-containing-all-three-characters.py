class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        res = [0] * 3
        i = 0
        c = 0
        l = 0
        while i < len(s):
            res[ord(s[i]) - ord('a')] += 1
            while res[0] > 0 and res[1] > 0 and res[2] > 0:
                c += len(s) - i
                res[ord(s[l]) - ord('a')] -= 1
                l += 1
            i += 1
        return c