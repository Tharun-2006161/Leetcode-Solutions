class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def GCD(x,y):
            if y==0:
                return x
            return GCD(y,x%y)
        odd=n*n
        even=n*(n+1)
        return GCD(odd,even)