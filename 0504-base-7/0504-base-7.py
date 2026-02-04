class Solution:
    def convertToBase7(self, num: int) -> str:
        p=[]
        org=num
        num=abs(num)
        if num==0:
            return "0"
        while(num>0):
            r=num%7
            p.append(str(r))
            num=num//7
        p.reverse()
        if org<0:
            return "-"+"".join(p)
        else:
            return "".join(p)
        