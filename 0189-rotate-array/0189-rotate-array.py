class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def rotation(nums,l,r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1
        n = len(nums)
        k = k % n
        rotation(nums, 0, n - 1)
        rotation(nums, 0, k - 1)
        rotation(nums, k, n - 1)
        