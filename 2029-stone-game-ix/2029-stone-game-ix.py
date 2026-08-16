class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        cnt = [0,0,0]
        for i in range(len(stones)):
            cnt[stones[i] % 3] += 1
        a = cnt[0]
        b = cnt[1]
        c = cnt[2]
        if a % 2 == 0:
            return b > 0 and c > 0
        return abs(b - c) > 2