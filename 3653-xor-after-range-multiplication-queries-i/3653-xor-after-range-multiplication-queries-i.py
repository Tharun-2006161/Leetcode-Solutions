class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        m=10**9 + 7
        for i in queries:
            li,ri,ki,vi = i
            idx=li
            while idx<=ri:
                nums[idx]=(nums[idx]*vi)%m
                idx+=ki
        res=0
        for i in nums:
            res^=i
        return res

