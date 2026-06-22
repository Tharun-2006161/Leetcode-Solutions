class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        t="abllno"
        res=[0]*26
        for i in range(len(text)):
            if text[i] in t:
                res[ord(text[i])-ord('a')]+=1
        res[11]=res[11]//2
        res[14]=res[14]//2
        return min(res[0],res[1],res[11],res[13],res[14])

        

    