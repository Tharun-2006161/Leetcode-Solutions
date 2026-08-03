class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        mpp = {}
        for i in range(len(nums)):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1
        Flag = False
        for i, j in mpp.items():
            if j >= 2:
                Flag = True
                break
        return Flag 