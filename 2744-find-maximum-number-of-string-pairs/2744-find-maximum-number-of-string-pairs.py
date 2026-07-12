class Solution:
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        c = 0
        res={}
        for i in range(len(words)):
            words[i] = sorted(words[i])
            p = ("".join((words[i])))
            if p not in res:
                res[p]=1
            else:
                c+=1
        return c
