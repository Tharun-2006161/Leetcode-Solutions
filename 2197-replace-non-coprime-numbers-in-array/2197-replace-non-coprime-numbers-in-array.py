class Solution:
    def replaceNonCoprimes(self, nums: list[int]) -> list[int]:
        def gcd(a,b):
            while b:
                a, b = b , a % b
            return a
        
        def LCM(a,b):
            return (a * b) // gcd(a,b)

        st = []
        for i in range(len(nums)):
            num = nums[i]
            while len(st) > 0:
                l = st[-1]
                if gcd(l,num) == 1:
                    break
                st.pop()
                num = (LCM(l,num))
            st.append(num)
        return st