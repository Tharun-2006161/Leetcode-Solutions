class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if 1 <= nums[i] <= len(nums) and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return nums[i]
        return len(nums) + 1