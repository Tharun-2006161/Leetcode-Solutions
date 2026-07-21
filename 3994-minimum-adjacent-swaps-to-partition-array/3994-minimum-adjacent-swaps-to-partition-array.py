class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        p1 = 0
        p2 = 0
        p3 = 0
        res = 0
        i = 0
        while i<len(nums):
            if (nums[i] < a) and (p2 >= 0 or p3 >= 0):
                res += (p2 + p3)
                p1 += 1
            elif (a <= nums[i] <= b) and (p3 >= 0):
                res += p3
                p2 += 1
            else:
                p3 += 1
            i += 1
        print(p1,p2,p3)
        return res