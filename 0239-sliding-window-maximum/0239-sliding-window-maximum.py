class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        prefix = [float('-inf')]*n
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            if i % k == 0:
                prefix[i] = nums[i]
            else:
                prefix[i] = max(prefix[i - 1],nums[i])
        suffix = [float("-inf")] * n
        suffix[n - 1] = nums[n - 1]
        for i in range(len(nums) - 2, -1, -1):
            if (i + 1) % k == 0:
                suffix[i] = nums[i]
            else:
                suffix[i] = max(suffix[i + 1],nums[i])
        ans = []
        j = 0
        for i in range(k - 1,len(prefix)):
            ans.append(max(prefix[i],suffix[j]))
            j += 1
        return ans           