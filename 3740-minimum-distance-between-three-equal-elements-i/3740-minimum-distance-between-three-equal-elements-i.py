class Solution:
    def minimumDistance(self, nums: List[int]) -> int:
        n=len(nums)
        a=float('inf')
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    if nums[i]==nums[j]==nums[k]:
                        d=abs(i-j)+abs(j-k)+abs(k-i)
                        a=min(a,d)
        return a if a!=float('inf') else -1