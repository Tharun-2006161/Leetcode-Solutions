class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        if m == 1:
            return ["." * n]
        else:
            ans = []
            for i in range(m):
                res = ""
                for j in range(n):
                    if i == 0 or j == n - 1:
                        res += "."
                    else:
                        res += "#"
                ans.append(res)
            return ans