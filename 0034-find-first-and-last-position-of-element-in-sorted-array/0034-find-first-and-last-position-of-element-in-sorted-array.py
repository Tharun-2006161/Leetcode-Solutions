class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        # res=[-1,-1]
        # for i in range(res[0],len(nums)):
        #     if nums[i]==target:
        #         res[0]=i
        #         break
        # print(res)
        # for i in range(res[0],len(nums)):
        #     if nums[i]==target:
        #         res[1]=i
        #         break
        # return res
        if target not in nums:
            return [-1,-1]
        if len(nums)==1:
            return [0,0]
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        print(res)
        if len(res)==1:
            return res*2
        else:
            return [res[0],res[-1]]

        