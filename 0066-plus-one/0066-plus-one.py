class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        p="".join(map(str,digits))
        a=int(p)+1
        s=list(map(int,str(a)))
        return s
