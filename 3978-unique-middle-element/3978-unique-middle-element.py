class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        s = len(nums) // 2
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
        if res[nums[s]] == 1:
            return True
        else:
            return False