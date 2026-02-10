class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        c=Counter(str(n))
        m=min(c.values())
        p=[int(d) for d,f in c.items() if f==m]
        return min(p)