class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        
        res = {}
        for i in range(len(nums)):
            res[nums[i]] = res.get(nums[i], 0) + 1
        p = res[nums[0]]
        q = res[nums[-1]]
        if k == 1:
            ans = []
            for i,j in res.items():
                if j == 1:
                    ans.append(i)
            if ans:
                return max(ans)
            else:

                return -1
        elif k == len(nums):
            return max(nums)
        elif 1 < k < len(nums):
            if p == 1 and q == 1:
                return max(nums[0], nums[-1])
            elif p > 1 and q == 1:
                return nums[-1]
            elif p == 1 and q > 1:
                return nums[0]
            else:
                return -1
        else:
            return 0