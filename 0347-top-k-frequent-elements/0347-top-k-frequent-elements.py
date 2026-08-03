class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        mpp = {}
        for i in range(len(nums)):
            mpp[nums[i]] = mpp.get(nums[i], 0) + 1
        # st = sorted(mpp.items(), key = lambda x:(-x[1],x[0]))
        st = sorted(mpp.items(), key = lambda x:x[1], reverse = True)
        res1 = []
        for i in range(k):
            res1.append(st[i][0])

        return res1      