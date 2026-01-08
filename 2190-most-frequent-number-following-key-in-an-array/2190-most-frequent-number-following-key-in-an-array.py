class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        p = Counter()
        ma = 0
        ans = 0

        for i in range(len(nums) - 1):
            if nums[i] == key:
                p[nums[i + 1]] += 1
                if p[nums[i + 1]] > ma:
                    ma = p[nums[i + 1]]
                    ans = nums[i + 1]

        return ans
