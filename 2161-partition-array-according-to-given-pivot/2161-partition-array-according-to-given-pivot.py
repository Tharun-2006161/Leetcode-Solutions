class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        p=[]
        for i in range(len(nums)):
            if nums[i]<pivot:
                p.append(nums[i])
        for i in range(len(nums)):
            if nums[i]==pivot:
                p.append(nums[i])
        for i in range(len(nums)):
            if nums[i]>pivot:
                p.append(nums[i])
        return p