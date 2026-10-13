class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        nums.sort()
        i = 0
        j = len(nums) - 1
        c = 0
        while i < j:
            c += (nums[j] - nums[i])
            i += 1
            j -= 1
        if i == j:
            c += nums[i]
        return c
