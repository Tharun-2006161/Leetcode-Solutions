class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        def merge_sort(res):
            if len(res) <= 1:
                return res
            mid = len(res) // 2
            left_arr = merge_sort(res[:mid])
            right_arr = merge_sort(res[mid:])
            return merge(left_arr,right_arr)
        def merge(left_arr,right_arr):
            i = j = 0
            right_smaller = 0
            res1 = []
            while i < len(left_arr) and j < len(right_arr):
                if left_arr[i][0] > right_arr[j][0]:
                    right_smaller += 1
                    res1.append(right_arr[j])
                    j += 1
                else:
                    res1.append(left_arr[i])
                    ans[left_arr[i][1]] += right_smaller
                    i += 1
            while i < len(left_arr):
                res1.append(left_arr[i])
                ans[left_arr[i][1]] += right_smaller
                i += 1
            while j < len(right_arr):
                res1.append(right_arr[j])
                j += 1
            return res1
    
        ans = [0] * len(nums)
        res = []
        for i in range(len(nums)):
            res.append((nums[i],i))
        merge_sort(res)
        return ans
        
