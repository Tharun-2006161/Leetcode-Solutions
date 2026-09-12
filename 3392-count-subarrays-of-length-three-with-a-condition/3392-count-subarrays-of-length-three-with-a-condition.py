class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        

        cnt = 0
        if len(nums) < 3:
            return 0
        i = 0
        j = 1
        k = 2
        while i < len(nums) and j < len(nums) and k < len(nums):
            if (nums[i] + nums[k]) == ((nums[j]) / 2.0):
                
                cnt += 1
            i += 1
            j += 1
            k += 1
        return cnt