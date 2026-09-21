class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        c = 0
        mp = {0: 1}
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - goal in mp:
                c += mp[prefix - goal]
            mp[prefix] = mp.get(prefix, 0) + 1
        return c