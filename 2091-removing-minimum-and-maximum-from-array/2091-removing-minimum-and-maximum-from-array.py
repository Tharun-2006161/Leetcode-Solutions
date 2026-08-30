class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            return 1
        def Front(nums):
            c = 0
            ma = max(nums)
            mi = min(nums)
            F1 = False
            F2 = False
            for i in range(len(nums)):
                if nums[i] == ma:
                    F1 = True
                elif nums[i] == mi:
                    F2 = True
                elif F1 and F2:
                    break
                c += 1
            return c
        def Back(nums):
            c = 0
            ma = max(nums)
            mi = min(nums)
            F1 = False
            F2 = False
            for i in range(len(nums) - 1, -1, -1):
                if nums[i] == mi:
                    F1 = True
                elif nums[i] == ma:
                    F2 = True
                elif F1 and F2:
                    break
                c += 1
            return c
        def middle(nums):
            c = 0
            ma = max(nums)
            mi = min(nums)
            F1 = False
            F2 = False
            temp = 0
            for i in range(len(nums)):
                c += 1
                if nums[i] == mi or nums[i] == ma:
                    temp = i
                    break
            for i in range(len(nums) - 1, temp, -1):
                c += 1
                if nums[i] == mi or nums[i] == ma:
                    break
            return c
        return min(Front(nums),Back(nums),middle(nums))
            
