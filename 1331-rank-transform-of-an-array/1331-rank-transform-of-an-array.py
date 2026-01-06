class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        p=arr[:]
        s=set(p)
        a=sorted(s)
        l={}
        for i in range(len(a)):
            l[a[i]]=(i+1)
        t=[]
        for i in range(len(arr)):
            t.append(l[arr[i]])
        return t
