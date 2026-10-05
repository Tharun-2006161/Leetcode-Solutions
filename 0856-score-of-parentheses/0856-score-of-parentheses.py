class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        st = [0]
        for i in s:
            if i == "(":
                st.append(0)
            else:
                t = st.pop()
                if t == 0:
                    sc = 1
                else:
                    sc = max(sc, t * 2)
                st[-1] += sc
        return st[0]