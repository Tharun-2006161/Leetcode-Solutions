class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        n=len(strs)
        m=len(strs[0])
        c=0
        for j in range(m):
            for i in range(n-1):
                if strs[i][j] >strs[i+1][j]:
                    c+=1
                    break
        return c