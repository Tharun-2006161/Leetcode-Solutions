class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        # n=len(nums)
        # p=[]
        # s=2**(n)
        # for i in range(s):
        #     p.append(bin(i)[2:].zfill(n))
        # r=list(set(p)-set(nums))
        # return r[0]
        p=[]
        for i in range(len(nums)):
            if nums[i][i]=='0':
                p.append('1')
            else:
                p.append('0')
        return "".join(p)