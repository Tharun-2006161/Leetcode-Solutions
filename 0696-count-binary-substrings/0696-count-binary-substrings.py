class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        pl=0
        cl=1
        ans=0
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                cl+=1
            else:
                ans+=min(pl,cl)
                pl=cl
                cl=1
        ans+=min(pl,cl)
        return ans