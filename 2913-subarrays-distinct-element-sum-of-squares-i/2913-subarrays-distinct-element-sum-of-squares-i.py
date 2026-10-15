class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        c = 0
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                s = set(nums[i:j + 1])
                c += len(s) ** 2
        return c + len(nums)