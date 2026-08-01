class Solution:
    def distinctIntegers(self, n: int) -> int:

        s = {0:1}
        c = 0
        for i in range(n + 1):
            for j in range(1,i + 1):
                if i%j == 1 and j not in s:
                    s[j] = s.get(j,0) + 1
                    c += 1
        return c + 1