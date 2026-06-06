class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        total=sum(nums)
        res=[]
        left=0
        for i in range(len(nums)):
            right = total-left-nums[i]
            res.append(abs(left-right))
            left=left+nums[i]
        return res