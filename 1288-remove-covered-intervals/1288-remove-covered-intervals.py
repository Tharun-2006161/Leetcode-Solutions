class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # def fun(a,b):
        #     return a[0]<=b[0] and a[1]>=b[1]
        # p=sorted(intervals, key=lambda x:(x[0],-x[1]))
        # c=0
        # i=0
        # j=1
        # print(p)
        # st=[False]*len(p)
        # for i in range(len(p)):
        #     for j in range(i+1,len(p)):
        #         print(p[i],p[j])
        #         if fun(p[i],p[j]):
        #             st[j]=True
        # print(st)
        # return len(intervals) - sum(st)
        intervals.sort(key=lambda x:(x[0],-x[1]))
        res=[intervals[0]]
        for i,j in intervals[1:]:
            pl,pr=res[-1]
            if pl<=i and pr>=j:
                continue
            res.append([i,j])
        return (len(res))