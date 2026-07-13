class Solution:
    def countLargestGroup(self, n: int) -> int:
        res={}
        for i in range(1,n+1):
            temp = i
            s = 0
            while temp > 0:
                r = temp%10
                s = s+r
                temp = temp//10
            if s not in res:
                res[s]=[i]
            else:
                res[s].append(i)
        print(res)
        c=0
        max_len = max(len(lst) for lst in res.values())

        for i in res.values():
            if len(i) == max_len:
                c+=1

        return c
