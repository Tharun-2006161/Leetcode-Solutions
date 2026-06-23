class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        p=[]
        s=s.split()
        for i in s:
            if i.isdigit():
                p.append(int(i))
        for i in range(len(p)-1):
            if p[i]>=p[i+1]:
                return False
                break
        return True
