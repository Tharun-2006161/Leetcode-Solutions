class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        p=[-1]*n
        for i in range(len(nums)):
            if 1<=nums[i]<=n:
                p[nums[i]-1]=nums[i]
        for i in range(len(p)):
            if p[i]==-1:
                return i+1
        return n+1