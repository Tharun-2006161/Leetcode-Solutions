class Solution:
    def trailingZeroes(self, n: int) -> int:
        
        s = len(str(n))
        c = 0
        div = 5
        for i in range(s + 1):
            c += (n // div)
            div *= 5
        return c