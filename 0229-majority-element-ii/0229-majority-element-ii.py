class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        res = {}
        
        for i in range(n):
            res[nums[i]] = res.get(nums[i], 0) + 1

        res1 = []
        for i,j in res.items():
            if j > n // 3:
                res1.append(i)
        return res1