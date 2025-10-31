class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        p=Counter(nums)
        s=[]
        for i,j in p.items():
            if j==2:
                s.append(i)
        return s