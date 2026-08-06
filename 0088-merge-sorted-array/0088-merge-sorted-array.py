class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        while i < len(nums2) and m < len(nums1):
            nums1[m], nums2[i] = nums2[i], nums1[m]
            i += 1
            m += 1
        nums1.sort()