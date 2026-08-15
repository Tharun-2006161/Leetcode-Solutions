class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        res = []
        prefix = 0
        for i in range(len(nums)):
            prefix = prefix ^ nums[i]
            res.append(prefix)
        print(res)
        if res[-1] != 0:
            return len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] != 0:
                return len(nums) - 1
        return 0