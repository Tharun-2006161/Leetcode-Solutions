class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        element = None
        c = 0
        for i in nums:
            if c == 0:
                element = i
                c += 1
            elif i == element:
                c += 1
            else:
                c -= 1
        return element