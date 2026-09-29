class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        i = 0
        j = 0
        c = 0
        while j < len(s):
            mp[s[j]] = mp.get(s[j], 0) + 1
            while ((j - i + 1) - max(mp.values())) > k:
                mp[s[i]] -= 1
                i += 1
            c = max((j - i + 1), c)
            j += 1
        return c
            