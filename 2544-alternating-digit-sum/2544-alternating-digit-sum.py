class Solution:
    def alternateDigitSum(self, n: int) -> int:
        p=str(n)
        sign=1
        ans=0
        for i in p:
            ans+=sign*int(i)
            sign=sign*(-1)
        return ans