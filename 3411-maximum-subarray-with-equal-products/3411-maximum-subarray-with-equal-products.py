class Solution:
    def maxLength(self, nums: List[int]) -> int:

        def Gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def Lcm(a, b):
            return (a * b) // gcd(a, b)
        ma = 0
        for i in range(len(nums)):
            p = 1
            g = 0
            l = 1
            for j in range(i, len(nums)):
                p *= nums[j]
                g = Gcd(g, nums[j])
                l = Lcm(l, nums[j])
                if p == (l * g):
                    ma = max(ma, j - i + 1)
                
        return ma

