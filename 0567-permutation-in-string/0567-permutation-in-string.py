class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        p = {}
        for i in range(len(s1)):
            p[s1[i]] = p.get(s1[i], 0) + 1
        i = 0
        res = {}
        while i < (len(s2) - len(s1) + 1):
            j = i
            while j < len(s1) + i:
                res[s2[j]] = res.get(s2[j], 0) + 1
                j += 1
            print(res)
            if res == p:
                return True
                break
            else:
                res = {}
                i += 1
        return False


        