class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        c=0
        s=list(set(word.lower()))
        for i in range(len(s)):
            if s[i].lower() in word and s[i].upper() in word:
                if (word.index(s[i].lower()) <word.index(s[i].upper())) and (s[i].lower() not in word[word.index(s[i].upper())+1:]):
                    c+=1
        return c