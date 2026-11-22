class Solution:
    def checkString(self, s: str) -> bool:
        if "a" not in s or ("b" not in s):
            return True
        
        i = 0
        while i < len(s):
            if s[i] == "b":
                for j in range(i + 1, len(s)):
                    if s[j] == "a":
                        return False
            i += 1
        return True