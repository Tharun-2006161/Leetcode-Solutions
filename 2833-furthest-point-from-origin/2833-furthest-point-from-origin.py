class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        l,r,d=0,0,0
        for i in range(len(moves)):
            if moves[i]=="L":
                l+=1
            elif moves[i]=="R":
                r+=1
            else:
                d+=1
        return max(l+d-r,r+d-l)