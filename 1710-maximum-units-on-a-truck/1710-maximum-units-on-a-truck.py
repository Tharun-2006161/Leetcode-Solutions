class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key = lambda x : x[1], reverse = True)
        ans = 0
        for i, j in boxTypes:
            if truckSize - i >= 0:
                ans += (i * j)
                truckSize -= i
            elif truckSize - i < 0:
                ans += truckSize * j
                break
        return ans 