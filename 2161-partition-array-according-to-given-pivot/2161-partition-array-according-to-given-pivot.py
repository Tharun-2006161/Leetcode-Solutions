class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        # p=[]
        # for i in range(len(nums)):
        #     if nums[i]<pivot:
        #         p.append(nums[i])
        # for i in range(len(nums)):
        #     if nums[i]==pivot:
        #         p.append(nums[i])
        # for i in range(len(nums)):
        #     if nums[i]>pivot:
        #         p.append(nums[i])
        # return p
        p=[pivot]*len(nums)
        i=0
        j=len(nums)-1
        l=0
        r=len(nums)-1
        while i<len(nums) and j>=0:
            if nums[i]<pivot:
                p[l]=nums[i]
                l+=1
               
            if nums[j]>pivot:
                p[r]=nums[j]
                r-=1
            i+=1
            j-=1
        return p