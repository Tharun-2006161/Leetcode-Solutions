class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        m=10**9+7
        def rev(x):
            return int(str(x)[::-1])
        c={}
        res=0
        for i in nums:
            d=i-rev(i)
            if d in c:
                res=(res+c[d])%m
                c[d]+=1
            else:
                c[d]=1
        return res