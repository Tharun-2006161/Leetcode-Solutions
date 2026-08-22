class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        c = 0
        i = 0
        j = 1
        while i < len(timeSeries) and j < len(timeSeries):
            s = timeSeries[j] - timeSeries[i]
            if s < duration:
                c += s
            else:
                c += duration
            i += 1
            j += 1
        return c + duration