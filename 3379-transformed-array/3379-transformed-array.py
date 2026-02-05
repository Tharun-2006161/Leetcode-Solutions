class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        p=[0]*len(nums)
        n=len(nums)
        for i in range(len(nums)):
           a=(i+nums[i])%n
           p[i]=nums[a]
        return p