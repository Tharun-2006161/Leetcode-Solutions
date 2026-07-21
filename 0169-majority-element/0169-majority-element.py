class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        n = len(nums)
        element = None
        count = 0
        for i in nums:
            if count == 0:
                element = i
                count += 1
            elif i != element:
                count -= 1
            else:
                count += 1
        return element