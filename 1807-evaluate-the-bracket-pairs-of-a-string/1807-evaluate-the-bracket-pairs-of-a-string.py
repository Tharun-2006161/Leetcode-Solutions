class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        stt = ""
        mp = {}
        for i, j in knowledge:
            mp[i] = j
        t = 0
        i = 0
        res = []
        while i < len(s):
            if s[i] == "(":
                j = i + 1
                st = ""
                while j < len(s):
                    if s[j] == ")":
                        break
                    st += s[j]
                    j += 1
                if st in mp:
                    stt += (mp[st])
                else:
                    stt += "?"
                i += (j - i + 1)
            
            else:
                stt += s[i]
                i += 1
        return stt
                    