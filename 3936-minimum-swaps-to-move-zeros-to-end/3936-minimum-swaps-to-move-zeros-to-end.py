class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        
        p = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                p += 1
        if p == 0:
            return 0
        else:
            res = nums[-p:]
            c = 0
            for i in res:
                if i != 0:
                    c += 1
            return c