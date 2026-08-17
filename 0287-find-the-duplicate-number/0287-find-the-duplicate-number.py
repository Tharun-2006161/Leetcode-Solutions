class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
        for i,j in res.items():
            if j > 1:
                return i