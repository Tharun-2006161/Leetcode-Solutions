class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        
        cnt = 0
        s = "aeiou"
        for k in range(len(word)):
            if word[k] not in s:
                continue
            a, e, i, o, u = 0, 0, 0, 0, 0
            for j in range(k, len(word)):
                if word[j] == "a":
                    a += 1
                elif word[j] == "e":
                    e += 1
                elif word[j] == "i":
                    i += 1
                elif word[j] == "o":
                    o += 1
                elif word[j] == "u":
                    u += 1
                else:
                    break
                if a > 0 and e > 0 and i > 0 and o > 0 and u > 0:
                    cnt += 1
        return cnt
                   