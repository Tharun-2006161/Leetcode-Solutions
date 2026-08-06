class Solution:
    def trap(self, height: List[int]) -> int:
        lm = []
        rm = [0] * len(height)
        lm1 = 0
        for i in range(len(height)):
            lm1 = max(lm1, height[i])
            lm.append(lm1)
        rm1 = 0
        for i in range(len(height) - 1, -1, -1):
            rm1 = max(rm1, height[i])
            rm[i] = rm1
        c = 0
        for i in range(len(height)):
            s = min(lm[i], rm[i])
            c += (s - height[i])
        return c

