class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        gs = nums[0]
        cm = nums[0]
        cmi = nums[0]
        for i in range(1, len(nums)):
            st = nums[i]
            sts = cm
            cm = max(st, st * sts, st * cmi)
            cmi = min(st, st * sts, st * cmi)
            gs = max(gs, cm)
        return gs