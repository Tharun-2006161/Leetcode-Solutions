class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        def fun(a,weights):
            s=0
            for i in range(len(a)):
                s+=weights[ord(a[i])-ord('a')]
            return s
        p=[]
        for i in range(len(words)):
            p.append((fun(words[i],weights))%26)
        print(p)
        t="zyxwvutsrqponmlkjihgfedcba"
        a=""
        for i in range(len(p)):
            a+=t[p[i]]
        return a

