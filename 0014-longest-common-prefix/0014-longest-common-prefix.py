class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        # def prefix(a,b):
        #     i = 0
        #     res = ""
        #     while i<len(a) and i<len(b):
        #         if a[i] != b[i]:
        #             break
        #         else:
        #             res += a[i]
        #         i += 1
        #     return res
        
        # if len(strs) < 2:
        #     return strs[0]
        # p = prefix(strs[0],strs[1])
        # for i in range(2,len(strs)):
        #     p = prefix(p,strs[i])
        # return p

        for i in range(len(strs[0])):
            for j in range(1,len(strs)):
                if i == len(strs[j]) or strs[j][i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]