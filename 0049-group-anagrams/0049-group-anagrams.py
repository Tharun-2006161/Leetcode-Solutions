class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = {}

        for i in range(len(strs)):
            t = "".join(sorted(strs[i]))
            if t not in res:
                res[t] = [strs[i]]
            else:
                res[t].append(strs[i])
        
        res1 = []

        for i,j in res.items():
            res1.append(j)
            
        return res1

        