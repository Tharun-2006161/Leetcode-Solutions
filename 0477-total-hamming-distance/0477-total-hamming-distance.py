class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:

        
        c = 0
        for i in range(32):
            ones = 0
            for t in nums:
                if (t >> i)    & 1:
                    ones += 1
            zeros = len(nums) - ones
            c += ones * zeros
        return c