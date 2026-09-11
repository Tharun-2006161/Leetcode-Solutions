class Solution:
    def maxDifference(self, s: str) -> int:
        res = {}
        for i in range(len(s)):
            res[s[i]] = res.get(s[i], 0) + 1
        even = []
        odd = []
        for i, j in res.items():
            if j % 2 == 0:
                even.append(j)
            else:
                odd.append(j)
        
        ma = max(odd)
        max_sum = float('-inf')
        for i in range(len(even)):
            max_sum = max(max_sum, ((ma - even[i])))
        return max_sum