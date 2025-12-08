class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p=0
        m={0:1}
        c=0
        for i in nums:
            p+=i
            if (p-k) in m:
                c+=m[p-k]
            m[p]=m.get(p,0)+1
        return c