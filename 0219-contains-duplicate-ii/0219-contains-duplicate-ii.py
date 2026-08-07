class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        s = set()
        l = 0
        for i in range(len(nums)):
            if nums[i] in s:
                return True
            else:
                s.add(nums[i])
            if i - l >= k:
                s.remove(nums[l])
                l += 1
        return False

