class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        def minimum(nums):
            ns = [len(nums)] * len(nums)
            st = []
            for i in range(len(nums)):
                while st and nums[st[-1]] >= nums[i]:
                    ns[st.pop()] = i
                st.append(i)
            ps = [-1] * len(nums)
            st1 = []
            for i in range(len(nums) - 1, -1, -1):
                while st1 and nums[st1[-1]] > nums[i]:
                    ps[st1.pop()] = i
                st1.append(i)
            res = 0
            for i in range(len(nums)):
                left = i - ps[i]
                right = ns[i] - i
                res += (left * right * nums[i])
            return res
        
        def maximum(nums):
            ns = [len(nums)] * len(nums)
            st = []
            for i in range(len(nums)):
                while st and nums[st[-1]] <= nums[i]:
                    ns[st.pop()] = i
                st.append(i)
            ps = [-1] * len(nums)
            st1 = []
            for i in range(len(nums) - 1, -1, -1):
                while st1 and nums[st1[-1]] < nums[i]:
                    ps[st1.pop()] = i
                st1.append(i)
            res = 0
            for i in range(len(nums)):
                left = i - ps[i]
                right = ns[i] - i
                res += (left * right * nums[i])
            return res
        
        return maximum(nums) - minimum(nums)