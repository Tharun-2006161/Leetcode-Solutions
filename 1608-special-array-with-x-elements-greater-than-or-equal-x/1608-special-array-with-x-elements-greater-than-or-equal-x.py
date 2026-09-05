class Solution:
    def specialArray(self, nums: List[int]) -> int:

        if len(nums) == 1 and nums[0] == 0:
            return -1
        elif len(nums) == 1 and nums[0] != 0:
            return 1
        cs = {}
        for i in range(min(nums) - 1,max(nums) + 1):
            c = 0
            for j in range(len(nums)):
                if i <= nums[j]:
                    c += 1
            cs[i] = c
        for i, j in cs.items():
            if i == j:
                return i
        return -1