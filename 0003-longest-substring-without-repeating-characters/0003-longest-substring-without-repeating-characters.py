class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        ma = 0
        l = 0
        st = set()
        for i in range(len(s)):
            while s[i] in st:
                st.remove(s[l])
                l += 1
            st.add(s[i])
            ma = max(ma, len(st))
        return ma