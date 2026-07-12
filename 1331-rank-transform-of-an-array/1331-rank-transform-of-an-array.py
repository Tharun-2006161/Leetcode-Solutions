class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        s=sorted(arr)
        res={}
        r=1
        for i in s:
            if i not in res:
                res[i] = r
                r+=1
        result=[]
        for i in range(len(arr)):
            result.append(res[arr[i]])
        return result