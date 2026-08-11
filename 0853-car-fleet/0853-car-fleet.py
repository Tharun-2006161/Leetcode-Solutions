class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        res = []
        for i in range(len(position)):
            res.append((position[i],((target - position[i]) / speed[i])))
        res1 = sorted(res,key = lambda x : x[0],reverse = True)
        res2 = []
        for i in range(len(res1)):
            res2.append(res1[i][1])
        c = 1
        prev = res2[0]
        for i in range(1,len(res2)):
            if res2[i] <= prev:
                continue
            else:
                c += 1
                prev = res2[i]
        return c