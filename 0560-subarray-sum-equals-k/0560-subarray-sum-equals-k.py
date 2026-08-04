class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        result = {0:1}
        count = 0
        prefix_sum = 0
        for i in range(len(nums)):
            prefix_sum += nums[i]
            remove = prefix_sum - k
            count += result.get(remove,0)
            result[prefix_sum] = result.get(prefix_sum,0) + 1
        return count

            