class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        st = -1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                st = (i - 1)
                break
        if st == -1:
            nums.reverse()
            return 
        i = len(nums) - 1
        while i > 0 and i != st:
            if nums[i] > nums[st]:
                nums[i], nums[st] = nums[st], nums[i]
                break
            i -= 1
        
        i = st + 1
        j = len(nums) - 1
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        



        