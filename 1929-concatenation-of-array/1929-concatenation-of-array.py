class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        p = nums
        for i in range(len(nums)):
            p.append(nums[i])
        return p