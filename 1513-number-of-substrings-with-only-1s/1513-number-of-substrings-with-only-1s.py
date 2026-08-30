class Solution:
    def numSub(self, s: str) -> int:
        res = ""
        c = 0
        for i in range(len(s)):
            if s[i] == "0":
                c += (len(res) * (len(res) + 1)) // 2
                res = ""
            else:
                res += s[i]
        c += (len(res) * (len(res) + 1)) // 2
        return c % (10 ** 9 + 7)

