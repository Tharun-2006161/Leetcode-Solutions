class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        
        if k == 1:
            return 0
        nums.sort(reverse = True)
        s = float('inf')
        for r in range(len(nums) - k + 1):
            s = min(s, nums[r] - nums[r + k - 1])
        return s