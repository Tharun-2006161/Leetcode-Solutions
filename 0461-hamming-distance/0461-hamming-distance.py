class Solution:
    def hammingDistance(self, x: int, y: int) -> int:

        p = bin(x)[2:].zfill(32)
        q = bin(y)[2:].zfill(32)
        c = 0

        i = 0
        
        while i < len(p):

            if p[i] != q[i]:
                c += 1

            i+=1

        return c
            





        