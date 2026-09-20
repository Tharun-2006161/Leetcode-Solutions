class Solution:
    def reverseDegree(self, s: str) -> int:
        c = 0
        for i in range(len(s)):
            c += ((97 - ord(s[i]) + 26)) * (i + 1)
        return c