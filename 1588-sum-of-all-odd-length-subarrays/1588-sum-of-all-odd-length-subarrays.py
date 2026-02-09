class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        n=len(arr)
        p=0
        for i in range(n):
            for j in range(i,n):
                l=j-i+1
                if l%2==1:
                    p+=sum(arr[i:j+1])
        return p