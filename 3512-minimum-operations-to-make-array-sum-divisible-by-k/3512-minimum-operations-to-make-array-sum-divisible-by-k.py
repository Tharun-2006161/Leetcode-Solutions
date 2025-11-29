class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        s=sum(nums)
        k=s%k
        return k
        if r==0:
            return 0
        else:
            return 1
