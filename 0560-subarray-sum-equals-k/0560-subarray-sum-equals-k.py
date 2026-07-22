class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        mpp = {0:1}
        prefix_sum = 0
        ans = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remove = prefix_sum - k
            ans += mpp.get(remove,0)
            mpp[prefix_sum] = mpp.get(prefix_sum,0) + 1
        return ans
            