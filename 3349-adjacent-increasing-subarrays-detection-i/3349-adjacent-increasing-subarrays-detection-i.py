class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        if 2*k>len(nums):
            return False
        def fun(a):
            for i in range(len(a)-1):
                if a[i]>=a[i+1]:
                    return False
            return True
        n=len(nums)
        for i in range(n-2*k+1):
            f=nums[i:i+k]
            s=nums[i+k:i+2*k]
            if fun(f) and fun(s):
                return True
        return False   