class Solution:
    def countHomogenous(self, s: str) -> int:
        MOD = (10 ** 9 + 7)
        res = []
        c = 0
        res.append(s[0])
        for i in range(1,len(s)):
            if res and s[i] != res[-1]:
                c += (len(res) * (len(res) + 1) // 2)
                res = []
                res.append(s[i])
            else:
                res.append(s[i])
        if res:
            c += (len(res) * (len(res) + 1) // 2)
        return c % MOD
            
