class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        mi = 999999999
        i = 0
        j = 0
        prefix = 0
        while i < len(nums) and j < len(nums):
            prefix += nums[i]
            while prefix >= target:
                mi = min(mi, i - j + 1)
                prefix -= nums[j]
                j += 1
            i += 1
        if mi != 999999999:
            return mi
        else:
            return 0
            
            