class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        s = []
        c = 0
        res = ["+", "-", "/", "*"]
        for i in tokens:
            if i not in res:
                s.append(int(i))
            else:
                st = s.pop()
                p = s.pop()
                if i == "+":
                    s.append(p + st)
                elif i == "-":
                    s.append(p - st)
                elif i == "*":
                    s.append(p * st)
                elif i == "/":
                    s.append(int(p / st))
        return s[-1]
           
        
