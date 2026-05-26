class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        a=set(word.lower())
        b=set(word)
        print(a,b)
        for i in a:
            print(i)
            print(b)
            if i.lower() in b:
                if i.upper() in b:
                    c+=1
        return c