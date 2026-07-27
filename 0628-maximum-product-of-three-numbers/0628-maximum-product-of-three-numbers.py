class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        m1 = float('-inf')
        m2 = float('-inf')
        m3 = float('-inf')
        mi1 = float('inf')
        mi2 = float('inf')
        for i in range(len(nums)):
            if nums[i] > m1:
                m3 = m2
                m2 = m1
                m1 = nums[i]
            elif nums[i] > m2:
                m3 = m2
                m2 = nums[i]
            elif nums[i] > m3:
                m3 = nums[i]

            if nums[i] < mi1:
                mi2 = mi1
                mi1 = nums[i]
            elif nums[i] < mi2:
                mi2 = nums[i]
        print(mi1,mi2,m1)
        print(m1,m2,m3)
        
        return max((mi1*mi2*m1),(m1*m2*m3))