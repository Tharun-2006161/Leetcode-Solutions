class Solution:
    def freqAlphabets(self, s: str) -> str:

        
        p=list(s)

        res = ""
        t=""
        res1=""
        for i in range(len(p)):

            if p[i] != "#":
                t += (p[i])

            elif p[i] == "#":
                for i in t[:-2]:
                    res+=chr(97+int(i)- 1)
                res += chr(97 + int(t[-2:]) - 1)
                t=""  
        
        for i in t:

            res += chr(97 + int(i) - 1)



        return (res)
        