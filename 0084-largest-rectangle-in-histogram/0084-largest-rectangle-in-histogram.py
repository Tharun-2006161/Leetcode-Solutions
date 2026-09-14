class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        previous_smaller = [-1] * len(heights)
        next_smaller = [len(heights)] * len(heights)
        st = []
        for i in range(len(heights) - 1, -1, -1):
            while st and heights[st[-1]] > heights[i]:
                previous_smaller[st.pop()] = i
            st.append(i)
        st = []
        for i in range(len(heights)):
            while st and heights[st[-1]] > heights[i]:
                next_smaller[st.pop()] = i
            st.append(i)
        ma = 0
        for i in range(len(heights)):
            area = heights[i] * (next_smaller[i] - previous_smaller[i] - 1)
            ma = max(ma, area)
        return ma