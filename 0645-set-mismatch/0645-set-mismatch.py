class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        i = 0
        n = len(nums)
        while i < n:
            ct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[ct]:
                nums[i], nums[ct] = nums[ct], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                return [nums[i], i + 1]