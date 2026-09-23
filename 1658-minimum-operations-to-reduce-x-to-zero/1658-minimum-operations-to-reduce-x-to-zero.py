class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        prefix = [0] * len(nums)
        pr = 0
        for i in range(len(nums)):
            pr += nums[i]
            prefix[i] = pr
        s = prefix[-1] - x
        if prefix[-1] < x:
            return -1
        r = 0
        l = 0
        c = 0
        ma = float('inf')
        while r < len(prefix):
            c += nums[r]
            
            while c > s and l < len(prefix):
                c -= nums[l]
                l += 1
            if c == s:
                ma = min(len(nums) - (r - l + 1), ma)
            r += 1
        if ma != float('inf'):
            return ma
        else:
            return -1

                    
