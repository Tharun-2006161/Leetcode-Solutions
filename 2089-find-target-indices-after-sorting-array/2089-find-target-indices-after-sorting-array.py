class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        p=sorted(nums)
        s=[]
        for i in range(len(p)):
            if p[i]==target:
                s.append(i)
        return s