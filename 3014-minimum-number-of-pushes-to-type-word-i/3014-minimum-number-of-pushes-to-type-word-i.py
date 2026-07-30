class Solution:
    def minimumPushes(self, word: str) -> int:
        res = [8,16,24,32,48]
        c = 0
        if len(word) < 8:
            return len(word)
        else:
            r = len(word) // 8
            p = len(word) % 8
            print(r,p)
            if r > 1:
                return sum(res[:r]) + (p *(r + 1))
            else:
                return (r) * 8 + (p *(r + 1))