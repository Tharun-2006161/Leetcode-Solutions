class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums2)
        for i in range(len(nums2) - 1, -1 , -1):
            while stack and stack[-1] <= nums2[i]:
                stack.pop()
            if stack:
                ans[i] = stack[-1]
            stack.append(nums2[i])
        res = []
        for i in range(len(nums1)):
            s = nums2.index(nums1[i])
            res.append(ans[s])
        return res