class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        prefix = 0
        for i in range(len(nums)):
            prefix = prefix ^ nums[i]
        
        if prefix != 0:
            return len(nums)
        
        for i in range(len(nums)):
            if nums[i] != 0:
                return len(nums) - 1
        return 0