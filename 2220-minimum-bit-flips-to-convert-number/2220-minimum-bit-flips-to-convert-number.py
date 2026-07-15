class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        
        p = bin(start)[2:].zfill(32)
        q = bin(goal)[2:].zfill(32)
        c = 0

        i = 0
        
        while i < len(p):

            if p[i] != q[i]:
                c += 1

            i+=1

        return c