class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in range(len(nums)):
            f[nums[i]]=f.get(nums[i],0)+1
        a=sorted(f.items(),key=lambda x:-x[1])
        print(a)
        t=[]
        for i in a:
            t.append(i[0])
        return (t[:k])
            