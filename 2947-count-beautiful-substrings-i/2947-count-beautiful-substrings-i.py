class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        
        ans = 0
        vowels = "aeiou"
        for i in range(len(s)):
            vc = 0
            cc = 0
            for j in range(i, len(s)):
                if s[j] in vowels:
                    vc += 1
                else:
                    cc += 1
                if vc == cc and (vc * cc) % k == 0:
                    ans += 1
        return ans
