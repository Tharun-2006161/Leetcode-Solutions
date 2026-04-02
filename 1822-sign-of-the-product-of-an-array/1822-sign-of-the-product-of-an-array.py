class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if 0 in nums:
            return 0
        else:
            for i in range(len(nums)):
                if nums[i]>0:
                    nums[i]=1
                else:
                    nums[i]=-1
            return (math.prod(nums))
        