class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        res = {}
        for i in range(len(nums)):
            n = target - nums[i]
            if n in res:
                return [res[n],i]
            res[nums[i]] = i
        return [-1,-1]
