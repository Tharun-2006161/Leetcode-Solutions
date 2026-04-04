class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]>=10:
                a=str((nums[i]))
                t=max(a)
                p=int(t*len(a))
                nums[i]=p
        return sum(nums)
                

