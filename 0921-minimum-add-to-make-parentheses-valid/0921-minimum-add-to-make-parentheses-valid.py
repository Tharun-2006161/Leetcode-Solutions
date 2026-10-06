class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        st = 0
        cnt = 0
        for i in s:
            if i == "(":
                st += 1
            elif i == ")" and st > 0:
                st -= 1
            elif st == 0 and i == ")":
                cnt += 1
        return cnt + st