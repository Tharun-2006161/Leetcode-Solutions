class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        
        st = set(nums)
        ma = 0
        for i in st:
            c = 1
            cur = i 
            while cur * cur in st:
                c += 1
                cur = cur * cur
            ma = max(ma,c)
        print(ma)
        if ma >= 2:
            return ma
        else:
            return -1
            