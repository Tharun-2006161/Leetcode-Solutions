class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        p = nums[-1]
        c = 0
        for i in range(len(nums) - 1):
            c += (p - nums[i])
        return c