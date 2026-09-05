class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        pm = [0] * len(nums)
        pmi = [0] * len(nums)
        prefix = 0
        for i in range(len(nums)):
            prefix = max(prefix, nums[i])
            pm[i] = prefix
        suffix = float('inf')
        for i in range(len(nums) - 1, -1, -1):
            suffix = min(suffix, nums[i])
            pmi[i] = suffix
        for i in range(len(nums)):
            if (pm[i] - pmi[i]) <= k:
                return i
        return -1