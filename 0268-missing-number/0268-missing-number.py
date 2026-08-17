class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = sum(nums)
        n = len(nums)
        ts = n * (n + 1) // 2
        return ts - s
