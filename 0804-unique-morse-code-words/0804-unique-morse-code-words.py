class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        p=[".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res=[]
        for i in words:
            a=""
            for j in i:
                a+=p[ord(j) - ord("a")]
            if a not in res:
                res.append(a)
        return len(res)