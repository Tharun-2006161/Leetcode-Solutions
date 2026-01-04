class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def divisors(n):
            r=[]
            for i in range(1,int(n**0.5) + 1):
                if n%i==0:
                    r.append(i)
                    if i!=n//i:
                        r.append(n//i)
            return r
        a=0
        for i in range(len(nums)):
            s=divisors(nums[i])
            if len(s)==4:
                a+=sum(s)
        if a:
            return a
        else:
            return 0