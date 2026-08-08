class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        s = 0
        l = 0
        c = float('inf')
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                c = min(c, i - l + 1)
                s -= nums[l]
                l += 1
        if c == float('inf'):
            return 0
        else:
            return c 