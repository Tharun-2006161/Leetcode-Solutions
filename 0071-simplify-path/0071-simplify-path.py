class Solution:
    def simplifyPath(self, path: str) -> str:
        s = path.split("/")
        # stack = []
        # for i in range(len(s)):
        #     if s[i] 
        st = []
        for i in range(len(s)):
            if s[i] == "" or s[i] == ".":
                continue
            elif s[i] == "..":
                if st:
                    st.pop()
            else:
                st.append(s[i])
        return "/" + "/".join(st)