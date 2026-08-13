class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        mpp = {}
        for i in range(len(nums)):
            if nums[i] not in mpp:
                mpp[nums[i]] = i
            else:
                if i - mpp[nums[i]] <= k:
                    return True
                else:
                    mpp[nums[i]] = i
        return False