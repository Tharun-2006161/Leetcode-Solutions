class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        p = {}
        for i in range(len(s1)):
            p[s1[i]] = p.get(s1[i], 0) + 1
        i = 0
        res = {}
        l = 0
        while i < (len(s2)):
            res[s2[i]] = res.get(s2[i],0) + 1
            while i - l + 1 > len(s1):
                res[s2[l]] -= 1
                if res[s2[l]] <= 0:
                    del res[s2[l]]
                l += 1
            print(res)
            if res == p:
                return True
                break   
            i += 1
        print(res)
        return False


        