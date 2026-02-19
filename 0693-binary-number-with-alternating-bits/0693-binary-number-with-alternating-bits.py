class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        p=bin(n)[2:]
        i=0
        j=1
        while i<len(p) and j<len(p):
            if p[i]==p[j]:
                return False
                break
            i+=1
            j+=1
        return True