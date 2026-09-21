class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        prefix = [0] * len(nums)
        p = 0
        for i in range(len(nums)):
            p += nums[i]
            prefix[i] = p
        c = 0
        for i in range(len(nums)):
            s = prefix[i] - k
            if s in mp:
                c += mp[s]
            mp[prefix[i]] = mp.get(prefix[i], 0) + 1
        return c