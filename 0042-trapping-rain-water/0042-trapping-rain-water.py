class Solution:
    def trap(self, height: List[int]) -> int:

        left_max = []
        right_max = [0]*len(height)
        ma = 0
        ma1 = 0
        
        for i in range(len(height)):
            ma = max(ma , height[i])
            left_max.append(ma)

        for i in range(len(height)-1,-1,-1):
            ma1 = max(ma1,height[i])
            right_max[i] = ma1

        c = 0
        for i in range(len(height)):
            s = min(left_max[i],right_max[i])
            c += (s - height[i])
        
        return c
        