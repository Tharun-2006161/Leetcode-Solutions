class Solution:
    def reverseParentheses(self, s: str) -> str:
        st = []
        for i in range(len(s)):
            if s[i] == ")":
                subst = ""
                while st and st[-1] != "(":
                    subst += st[-1]
                    st.pop()
                st.pop()
                print(subst)
                # subst = list(subst)
                # k = 0
                # l = len(subst) - 1
                # while k < l:
                #     subst[k], subst[l] = subst[l], subst[k]
                #     k += 1
                #     l -= 1
                # sub = "".join(subst)

                j = 0
                while j < len(subst):
                    st.append(subst[j])
                    j += 1
            else:
                st.append(s[i])
        return "".join(st)
                