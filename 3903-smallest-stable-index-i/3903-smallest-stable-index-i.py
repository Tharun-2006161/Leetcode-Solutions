class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        i = 0
        ma = 0
        t = 0
        while i < len(nums):
            ma = max(ma, nums[i])
            t = ma - min(nums[i:])
            if t <= k:
                return i
            i += 1
        return -1
