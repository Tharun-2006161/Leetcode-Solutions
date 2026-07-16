class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        
        def gcd(a,b):

            while b:
                a,b = b,a % b
            return a
        
        result = []
        mi = nums[0]

        for i in range(len(nums)):

            mi = max(mi,nums[i])
            result.append(gcd(nums[i] , mi))

        result1 = (sorted(result))
        
        if len(result1) == 1:
            return 0

        sum = 0
        i = 0
        j = len(result1)-1

        while i < j:
            sum += gcd(result1[i],result1[j])
            i+=1
            j-=1
        
        return sum
