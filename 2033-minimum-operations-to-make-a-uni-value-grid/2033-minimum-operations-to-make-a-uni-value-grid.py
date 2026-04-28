class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        p=[]
        for i in range(len(grid)):
            for j in range(len(grid)):
                p.append(grid[i][j])
        p.sort()
        m=len(p)//2
        s=0
        for i in range(len(p)):
            if abs(p[i]-p[m])%x!=0:
                return -1
            s+=abs(p[i]-p[m])//x
        return s