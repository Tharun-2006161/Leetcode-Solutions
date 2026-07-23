class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0 
        prefix_sum = 0
        mpp = {0:1}
        for i in range(len(nums)):
            prefix_sum += nums[i]
            div = prefix_sum % k
            count += mpp.get(div , 0) 
            mpp[div] = mpp.get(div,0) + 1
        return count


