class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)
        while low <= high:
            m = (low + high) // 2
            st = 1
            p = 0
            for i in nums:
                if p + i <= m:
                    p = p + i
                else:
                    st += 1
                    p = i
            if st <= k:
                high = m - 1
            else:
                low = m + 1
        return low