class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        mpp = {}
        l = 0
        ma = 0
        for i in range(len(nums)):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1
            while mpp[nums[i]] > k:
                mpp[nums[l]] -= 1
                l += 1
            ma = max(ma,i - l + 1)
        return ma