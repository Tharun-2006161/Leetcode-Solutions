class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        def fun(a,b):
            return a[0]<=b[0] and a[1]>=b[1]
        p=sorted(intervals, key=lambda x:(x[0],-x[1]))
        c=0
        i=0
        j=1
        print(p)
        st=[False]*len(p)
        for i in range(len(p)):
            for j in range(i+1,len(p)):
                if fun(p[i],p[j]):
                    st[j]=True
        return len(intervals) - sum(st)