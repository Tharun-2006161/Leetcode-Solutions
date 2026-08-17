class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma = 0
        c = 0
        for i in nums:
            if i == 1:
                c += 1
            else:
                ma = max(ma, c)
                c = 0
        ma = max(ma, c)
        return ma
        