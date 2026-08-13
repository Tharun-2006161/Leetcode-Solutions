class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        mpp = {}
        l = 0
        ma = 0
        for i in range(len(fruits)):
            mpp[fruits[i]] = mpp.get(fruits[i], 0) + 1
            while len(mpp) > 2:
                mpp[fruits[l]] -= 1
                if mpp[fruits[l]] == 0:
                    del mpp[fruits[l]]
                l += 1
            ma = max(ma, i - l + 1)
        return ma