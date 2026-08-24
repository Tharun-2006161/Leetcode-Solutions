class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        f1 = [0] * 26
        k = len(p)
        for i in p:
            f1[ord(i) - ord('a')] += 1
        f2 = [0] * 26
        for i in range(len(s)):
            f2[ord(s[i]) - ord('a')] += 1
            if i >= k:
                f2[ord(s[i - k]) - ord('a')] -= 1
            if i >= k - 1:
                if f1 == f2:
                    res.append(i - k + 1)
        return res
