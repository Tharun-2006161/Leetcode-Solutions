class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        
        def merge_sort(nums):
            if len(nums) <= 1:
                return nums
            mid = len(nums) // 2
            left_arr = merge_sort(nums[:mid])
            right_arr = merge_sort(nums[mid:])
            return merge(left_arr,right_arr)
        def merge(left_arr,right_arr):
            i = j = 0
            res = []
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i] < right_arr[j]:
                    res.append(left_arr[i])
                    i += 1
                else:
                    res.append(right_arr[j])
                    j += 1
            while i < len(left_arr):
                res.append(left_arr[i])
                i += 1
            while j < len(right_arr):
                res.append(right_arr[j])
                j += 1

            return res
        
        return merge_sort(nums)