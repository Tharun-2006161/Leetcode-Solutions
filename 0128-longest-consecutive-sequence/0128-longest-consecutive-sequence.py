class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        p = sorted(list(set(nums)))
        i = 0
        j = 1
        print(p)
        m = 0
        c = 1
        Flag = True
        while i < len(p) and j < len(p):
            if p[i] + 1 != p[j]:
                Flag = False
                m = max(m,c)
                c = 1
            else:
                c += 1
            i += 1
            j += 1
        m = max(c,m)
        if Flag:
            return len(p)
        else:
            return m