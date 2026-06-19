class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        ma=0
        t=ma
        for i in range(len(gain)):
            t+=gain[i]
            ma=max(ma,t)

        return ma