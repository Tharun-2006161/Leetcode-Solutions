class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return palindrome(i + 1, j) or palindrome(i, j - 1)

        return True