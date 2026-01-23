class Solution:
    def dayOfYear(self, date: str) -> int:
        def leap(f):
            t=int(f)
            if (t%400==0) or (t%4==0 and t%100!=0):
                return True
            return False
        p={"01":31,"02":28,"03":31,"04":30,"05":31,"06":30,"07":31,"08":31,"09":30,"10":31,"11":30,"12":31}
        a,b,c=map(str,date.split('-'))
        res=0
        for i,j in p.items():
            if i==b:
                res+=int(c)
                break
            else:

                res+=j
        if leap(a) and int(b)>2:
            res+=1
        return res
