class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        i=0
        j=len(nums)-1
        p=[]
        while i<len(nums) and j<len(nums):
            p.append(nums[i]+nums[j])
            i+=1
            j-=1
        return max(p)
            