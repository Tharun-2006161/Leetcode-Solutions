class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def fun(a):
            p=str(a)
            flag=True
            if "0" in p:
                flag=False
            else:
                for i in p:
                    if a%int(i)!=0:
                        flag=False
                        break
            return flag
        p=[]
        for i in range(left,right+1):
            if fun(i):
                p.append(i)
        return p
            