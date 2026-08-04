class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        t = list(set(nums))
        t.sort()
        i = 0
        c = 0
        ma = 0
        r = t[0]
        while i < len(t):
            if r == t[i]:
                c += 1
                r += 1
            elif r != t[i]:
                ma = max(ma,c)
                c = 1
                r = t[i] + 1
            i += 1
        ma = max(ma, c)
        return ma