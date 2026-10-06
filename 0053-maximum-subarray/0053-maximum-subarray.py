class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        gs = nums[0]
        ms = nums[0]
        for i in range(1, len(nums)):
            gs = max(nums[i], nums[i] + gs)
            ms = max(ms, gs)
        return ms