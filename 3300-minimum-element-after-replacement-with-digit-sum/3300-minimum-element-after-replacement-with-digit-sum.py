class Solution:
    def minElement(self, nums: List[int]) -> int:
        p=[]
        for i in range(len(nums)):
            s=0
            while nums[i]>0:
                r=nums[i]%10
                s=s+r
                nums[i]=nums[i]//10
            nums[i]=s
        return min(nums)
        