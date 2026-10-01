class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        for i in s:
            if i in "({[":
                st.append(i)
            elif i == ")" and st and st[-1] == "(":
                st.pop()
            elif i == "]" and st and st[-1] == "[":
                st.pop()
            elif i == "}" and st and st[-1] == "{":
                st.pop()
            else:
                return False
        return len(st) == 0