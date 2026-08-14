class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        mpp = {}
        ma = 0
        l = 0
        for i in range(len(s)):
            mpp[s[i]] = mpp.get(s[i], 0) + 1
            while mpp[s[i]] > 2:
                mpp[s[l]] -= 1
                l += 1
            lst = sum(list(mpp.values()))
            ma = max(lst,ma)
        lst1 = sum(list(mpp.values()))
        ma = max(lst1,ma)
        return ma