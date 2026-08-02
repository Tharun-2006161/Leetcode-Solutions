class Solution:
    def countSubstrings(self, s: str) -> int:
        # c = 0
        # for i in range(len(s)):
        #     for j in range(i + 1,len(s)):
        #         p = s[i : j + 1]
        #         if p == p[::-1]:
        #             c += 1
        # print(c + len(s))
        c = 0
        n = len(s)
        for i in range(2 * n - 1):
            l = i // 2
            r = (i + 1) // 2
            while l >= 0 and r < n and s[l] == s[r]:
                c += 1
                l -= 1
                r += 1
        return c