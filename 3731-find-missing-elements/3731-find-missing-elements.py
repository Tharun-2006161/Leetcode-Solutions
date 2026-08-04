class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums.sort()
        c = nums[0]
        res = []
        for i in range(c, max(nums)):
            if c not in nums:
                res.append(c)
                c += 1
            else:
                c += 1
        return res
            
        