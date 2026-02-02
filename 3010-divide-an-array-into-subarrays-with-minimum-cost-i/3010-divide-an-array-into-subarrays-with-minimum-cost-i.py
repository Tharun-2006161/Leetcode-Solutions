class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        p=nums[0]
        a=len(nums)
        s=nums[1:a]
        s.sort()
        return (p+s[0]+s[1])