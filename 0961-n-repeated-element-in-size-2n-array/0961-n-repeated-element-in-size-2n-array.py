class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        p=Counter(nums)
        m_c=max(p.values())
        m_cc=max(p,key=p.get)
        return m_cc
        