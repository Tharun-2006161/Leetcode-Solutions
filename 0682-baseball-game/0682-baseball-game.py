class Solution:
    def calPoints(self, operations: List[str]) -> int:
        p=[]
        for i in range(len(operations)):
            if operations[i]=="C":
                p.pop()
            elif operations[i]=="+":
                p.append(p[-1]+p[-2])
            elif operations[i]=="D":
                p.append(p[-1]*2)
            else:
                p.append(int(operations[i]))
        return sum(p)
       