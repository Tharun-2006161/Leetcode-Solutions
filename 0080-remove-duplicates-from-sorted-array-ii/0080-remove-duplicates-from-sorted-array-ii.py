class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j=1
        c=1
        n=len(nums)
        for i in range(1,n):
            if nums[i]==nums[i-1]:
                c+=1
            else:
                c=1
            if c<=2:
                nums[j]=nums[i]
                j+=1
        return j