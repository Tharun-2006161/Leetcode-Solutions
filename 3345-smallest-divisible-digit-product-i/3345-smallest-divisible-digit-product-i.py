class Solution:
    def smallestNumber(self, n: int, t: int) -> int:

        if n < t:
            return t

        st = 10 ** len(str(n)) -  1
        for temp in range(n, st + 2):
            c = 1
            i = temp
            print(i)
            while i > 0:
                r = i % 10
                c *= r
                i = i // 10
            print(c)
            if c % t == 0:
                return temp