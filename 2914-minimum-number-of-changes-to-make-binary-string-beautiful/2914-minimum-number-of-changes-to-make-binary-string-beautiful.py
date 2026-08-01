class Solution:
    def minChanges(self, s: str) -> int:
        i = 0
        j = 1
        c = 0
        while i < len(s) and j < len(s):
            if s[i] != s[j]:
                c += 1
            i += 2
            j += 2
        return c