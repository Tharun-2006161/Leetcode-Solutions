class Solution:
    def countCommas(self, n: int) -> int:
        p=str(n)
        if len(p)>3:
            return n-999
        else:
            return 0