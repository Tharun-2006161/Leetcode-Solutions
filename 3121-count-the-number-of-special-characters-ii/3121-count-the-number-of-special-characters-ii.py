class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        l={}
        u={}
        for i,ch in enumerate(word):
            if ch.islower():
                l[ch]=i
            else:
                if ch not in u:
                    u[ch]=i
        c=0
        for ch in l:
            if ch.upper() in u and l[ch] < u[ch.upper()]:
                c+=1
        return c
        