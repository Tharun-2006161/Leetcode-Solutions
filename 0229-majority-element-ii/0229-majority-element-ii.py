class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        first = None
        second = None
        c1 = 0
        c2 = 0
        for i in nums:
            if i == first:
                c1 += 1
            elif i == second:
                c2 += 1
            elif c1 == 0:
                first = i
                c1 += 1
            elif c2 == 0:
                second = i
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1
        ele1 = 0
        ele2 = 0
        for i in nums:
            if i == first:
                ele1 += 1
            elif i == second:
                ele2 += 1
        res = []
        if ele1 > n // 3:
            res.append(first)
        if ele2 > n // 3:
            res.append(second)
        return res
    