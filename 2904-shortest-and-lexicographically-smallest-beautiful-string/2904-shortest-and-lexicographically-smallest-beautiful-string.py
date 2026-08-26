class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        res = []
        l = 0
        r = []
        one = 0
        for i in range(len(s)):
            r.append(s[i])
            if s[i] == "1":
                one += 1
            if one == k:
                while r[l] != "1":
                    del r[l]
                t = "".join(r)
                if not res:
                    res.append(t)
                elif len(res[0]) < len(t):
                    pass
                elif len(res[0]) > len(t):
                    res[0] = t
                else:
                    old = res[0]
                    j = 0
                    while j < len(old):
                        if old[j] > t[j]:
                            res[0] = t
                            break
                        elif old[j] < t[j]:
                            break
                        else:
                            j += 1

                r.remove(r[0])
                one = k - 1
        if res:
            return res[0]
        else:
            return ""


                    
            

