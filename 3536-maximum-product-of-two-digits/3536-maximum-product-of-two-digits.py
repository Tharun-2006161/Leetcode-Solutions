class Solution:
    def maxProduct(self, n: int) -> int:
        p=list(str(n))
        a=sorted(p,reverse=True)
        return (int(a[0])*int(a[1]))