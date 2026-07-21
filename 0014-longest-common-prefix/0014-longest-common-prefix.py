class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        def prefix(a,b):
            i = 0
            res = ""
            while i<len(a) and i<len(b):
                if a[i] != b[i]:
                    break
                else:
                    res += a[i]
                i += 1
            return res
    
        if strs[0] == "":
            return ""
        if len(strs) == 1:
            return strs[0]
        p = prefix(strs[0],strs[1])

        if len(strs) == 2:
            return p
        else:
            for i in range(2,len(strs)):
                p = prefix(p,strs[i])
            return p

        