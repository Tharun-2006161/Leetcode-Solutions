class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        p=[]
        for i in range(len(A)):
            s=A[:i+1]
            t=B[:i+1]
            w=set(s)&set(t)
            p.append(len(w))
        return p