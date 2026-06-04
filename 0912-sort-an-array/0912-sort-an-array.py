class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(nums):
            n=len(nums)
            if n<=1:
                return
            mid=n//2
            left_arr = nums[:mid]
            right_arr=nums[mid:]
            merge(left_arr)
            merge(right_arr)
            i=0
            j=0
            k=0
            while i<len(left_arr) and j<len(right_arr):
                if left_arr[i]>right_arr[j]:
                    nums[k]=right_arr[j]
                    j+=1
                else:
                    nums[k]=left_arr[i]
                    i+=1
                k+=1
            while i<len(left_arr):
                nums[k]=left_arr[i]
                i+=1
                k+=1
            while j<len(right_arr):
                nums[k]=right_arr[j]
                j+=1
                k+=1
        merge(nums)
        return nums