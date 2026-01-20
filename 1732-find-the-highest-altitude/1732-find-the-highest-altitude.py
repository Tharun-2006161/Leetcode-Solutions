class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        gs=0
        cs=0
        for i in gain:
            cs+=i
            gs=max(gs,cs)
        return gs