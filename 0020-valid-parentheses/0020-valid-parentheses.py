class Solution:
    def isValid(self, s: str) -> bool:
        s1 = []
        for i in s:
            if i in "([{":
                s1.append(i)
            elif i == ")" and s1 and s1[-1] == "(":
                s1.pop()
            elif i == "]" and s1 and s1[-1] == "[":
                s1.pop()
            elif i == "}" and s1 and s1[-1] == "{":
                s1.pop()
            else:
                return False
        return len(s1) == 0