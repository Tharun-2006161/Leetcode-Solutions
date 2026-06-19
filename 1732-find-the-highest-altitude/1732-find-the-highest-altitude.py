class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res=[0]
        p=0
        for i in range(len(gain)):
            res.append(p+gain[i])
            p=p+gain[i]
        return max(res)
