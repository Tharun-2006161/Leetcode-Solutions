class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # res = []
        # for i in range(len(nums)):
        #     if nums[i] > 0:
        #         res.append(nums[i])
        # res.sort()
        # if res == []:
        #     return 1
        # c = 1
        # for i in range(len(res)):
        #     if c == res[i]:
        #         c += 1
        #     else:
        #         return c
        #         break
        # return len(nums)
        n = len(nums)
        i = 0
        while i < n:
            ct = nums[i] - 1
            if 1 <= nums[i] <= n and nums[i] != nums[ct]:
                nums[i], nums[ct] = nums[ct], nums[i]
            else:
                i += 1
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

