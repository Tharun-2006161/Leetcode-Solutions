class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:

        n = len(grid)
        for t in range(k):
            lst = grid[-1][-1]
            for i in range(n-1,-1,-1):
                for j in range(n-1,-1,-1):
                    if (i!=0 and j == 0):
                        grid[i][j] = grid[i-1][n-1]
                    else:
                        grid[i][j] = grid[i][j-1]
            grid[0][0] = lst
        return grid